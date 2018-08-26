'''运行一个最简单的web程序'''
from flask import Flask

app = Flask(__name__)

'''如果路由配置成  /hello/会重定向/hello'''


@app.route('/hello')
def hello():
    return 'hello flask'


def hello1():
    return 'hello flask1'


if __name__ == '__main__': #保证了在生产环境上不会去执行flask自带的测试开发服务器
    '''另一种路由注册的方式'''
    app.add_url_rule('/hello1', view_func=hello1)
    '''加入debug模式'''
    '''注意:debug模式只是在开发测试模式下的调试用,不能再生成环境设置debug模式'''
    '''如果采用from_object的方式来导入常量,config.py文件中的常量所有字母都必须为大写'''
    '''DEBUG是flask中的参数默认值'''
    '''下面的app.run()是flask自带的服务器,
       生产环境:nginx+uwsgi 
       nginx:作为前置服务器,把请求转发给uwsgi
       运行项目是靠uswsgi加载fisher.py这个模块'''
    app.config.from_object('config')
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000)
