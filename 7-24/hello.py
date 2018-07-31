from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello',methods=['GET','POST','PUT'])  #路由默认只支持GET,如果需要增加,需要自行指定,列表方式
def hello():
    return 'Hello, World'

@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
    return '大笨蛋 %s' % order_id


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)
