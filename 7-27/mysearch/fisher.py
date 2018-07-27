from flask import Flask,make_response
from helper import isbn_or_key

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')  
def search(q,page):
    '''
        q :普通关键字 isbn
        page
    '''
    isbn_or_key = is_isbn_or_key(q)

    if __name__ == '__main__':  
        app.run(host="0.0.0.0",port=8000,debug=True)

            