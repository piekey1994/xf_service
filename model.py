#coding:utf-8
from sql_config import Plugin
from sql_config import db
from datetime import datetime
def getAllPlugins():
    return Plugin.query.all()

def insertPlugin(unicode,name,info,author,pushtime,location,coverage):
    oldPlugin=Plugin.query.filter_by(name=name).first()
    if oldPlugin!=None:
        if oldPlugin.unicode!=unicode and coverage==1:
            db.session.delete(oldPlugin)
            db.session.commit()
        else:
            return
    newPlugin=Plugin(unicode=unicode,name=name,info=info,author=author,pushtime=datetime.strptime(pushtime, '%Y-%m-%d %H:%M:%S'),location=location,coverage=coverage)
    db.session.add(newPlugin)
    db.session.commit()
    #保存插件