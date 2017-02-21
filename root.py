from flask import Flask
from urllib import urlopen
app = Flask(__name__)

@app.route('/getlist')
def getlist():
    xunfengList=getXunfengList()
    mylist=getMyList()
    return xunfengList+mylist

def getXunfengList():
    f=urlopen('https://sec.ly.com/xunfeng/getlist')
    j=f.read()
    if j:
        return j
    return ''

def getMyList():
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0')
