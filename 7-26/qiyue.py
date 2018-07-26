from flask import Flask

__author__ = '七月'

app = Flask(__name__)


@app.route('/hello/')  #装饰器
def hello():
    #基于类的视图(即插视图)
    # 1/0    访问之后显示具体的错误
    return 'Hello QiYue'

# app.add_url_rule('hello',view_func=hello)   即插视图使用add_url_rule

if __name__ == '__main__':
   app.run(host="127.0.0.1",port=8000,debug=True)