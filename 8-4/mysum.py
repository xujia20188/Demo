from flask import Flask,url_for,request


app = Flask(__name__)


@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    request.form
    return "a+b={}".format(a+b)

if __name__ == '__main__':
    app.run(debug=True)