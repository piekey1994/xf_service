#coding:utf-8
from flask import Flask,render_template,request,send_from_directory,abort
from urllib import urlopen
from model import *
from datetime import datetime
from flask import jsonify
import os
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
    plugins=getAllPlugins()
    retjsonlist=[]
    for p in plugins:
        pdict={'unicode':p.unicode,
            'name':p.name,
            'info':p.info,
            'author':p.author,
            'pushtime':p.pushtime.strftime('%Y-%m-%d %H:%M:%S'),
            'location':p.location,
            'coverage':p.coverage}
        retjsonlist.append(pdict)
    return jsonify(retjsonlist)

@app.route('/getplugin')
def installplugin():
    #返回文件给它
    filename=request.args.get('name')
    if os.path.isfile(os.path.join('plugins', filename)):
        return send_from_directory('plugins',filename,as_attachment=True)
    abort(404)

def getXunfengList():
    f=urlopen('https://sec.ly.com/xunfeng/getlist')
    return f.read()


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
