from flask import Flask,make_response
from config import DEBUG


app = Flask(__name__)


@app.route('/hello')  #装饰器
def hello():
    #基于类的视图(即插视图)
    # 1/0    访问之后显示具体的错误

    headers ={
        'content-type':'text/plain',
        'location': 'http://www.bing.com'
    }
    response = make_response('<html></html>',301)
    response.headers = headers

    return  response




# app.add_url_rule('hello',view_func=hello)   即插视图使用add_url_rule

if __name__ == '__main__':   #生产环境
   app.run(host="0.0.0.0",port=8000,debug=DEBUG)