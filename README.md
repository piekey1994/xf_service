# 巡风后台
## 使用说明
### 添加依赖库

```
pip install flask
pip install flask-sqlalchemy

```
### 初始化sqlite

```
python initSql.py
```
### 开始web服务

```
sh Run.sh
```
### 访问页面
- 127.0.0.1:5000/update (手动更新巡风的插件列表，并查看目前已有到插件列表)
- 127.0.0.1:5000/getlist（对应巡风的sec.ly.com/xunfeng/getlist接口，返回最新到插件列表list）
- 127.0.0.1:5000/getplugin?name= （对应巡风的sec.ly.com/xunfeng/getplugin?name=接口，下载对应到插件文件）


## 代码结构
- model.py是存放数据库操作的
- View.py里面有几个页面都有注释
