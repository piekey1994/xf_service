#coding:utf-8
import json
from flask import Flask
from flask import render_template
from urllib import urlopen
from model import *
app = Flask(__name__)

@app.route('/update')
def update():
    plugins=getAllPlugins()
    return render_template('update.html',plugins=plugins)

@app.route('/updatelist')
def updatelist():
    xunfengList=getXunfengList()
    pluginList=xunfengList.strip()
    if pluginList:
        #try:
            remotelist = json.loads(pluginList)
            for i in remotelist:
                insertPlugin(i['unicode'],i['name'],i['info'],i['author'],i['pushtime'],i['location'],i['coverage'])
            return 'success'
        #except:
        #    return 'failed'

@app.route('/getlist')
def getlist():
    #读取数据库生存json文件
    return ''

@app.route('/installplugin')
def installplugin():
    #返回文件给它
    return ''

def getXunfengList():
    f=urlopen('https://sec.ly.com/xunfeng/getlist')
    return f.read()


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
