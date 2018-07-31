from flask import Flask,jsonify


app = Flask(__name__)
app.config.from_object('config')

if __name__ == '__main__':  
    print(id(app))
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=81)