from flask import Flask,jsonify


app = Flask(__name__)


@app.route('/hello')  #装饰器
def hello():
    return jsonify({"message":"hello"})




# app.add_url_rule('hello',view_func=hello)   即插视图使用add_url_rule

if __name__ == '__main__':   #生产环境
   app.run(host="0.0.0.0",port=5000,debug=True)