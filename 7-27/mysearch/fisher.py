from flask import Flask,make_response

__author__ = '七月'

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')  
def search(q,page):
    '''
        q :普通关键字 isbn
        page
    '''

    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    short_q = q.replace('_','')
    if '-' in q and len(short_q) == 10 and short_q.isdigit:
        isbn_or_key='isbn'
    pass

    if __name__ == '__main__':  
        app.run(host="0.0.0.0",port=8000,debug=True)