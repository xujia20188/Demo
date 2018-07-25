from flask import Flask

__author__='七月'

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'


app.run()