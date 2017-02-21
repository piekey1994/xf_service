from flask import Flask
from urllib.request import urlopen
app = Flask(__name__)

@app.route('/getlist')
def getlist():
    xunfengList=getXunfengList()
    mylist=getMyList()
    return xunfengList+mylist

def getXunfengList():
    return urlopen('https://sec.ly.com/xunfeng/getlist')

def getMyList():
    return ''


if __name__ == '__main__':
    app.run()