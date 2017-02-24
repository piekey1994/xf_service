#coding:utf-8
from sql_config import Plugin
from sql_config import db
from datetime import datetime
import logging
from urllib import urlretrieve
import os

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='model.log',
                filemode='w')

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
    #保存插件
    if location.find('/') == -1:
        urlretrieve('https://sec.ly.com/xunfeng/getplugin?name=' + location, 'plugins/' + location)
    else:
        urlretrieve(location, 'plugins/' + location)  # 兼容旧的插件源
    if os.path.exists('plugins/' + location):
        logging.info('plugin '+unicode+' download success')
        db.session.commit()
    else:
        logging.warning('plugin '+unicode+' download failed')

