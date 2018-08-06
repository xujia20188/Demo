from http import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}`'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}'
    
    @classmethod        #定义为静态
    def search_by_isbn(cls,isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HTTP.get(cls,url)
        return cls(result)
     

    @classmetho
    def search_by_keyword(cls,keyword):
        url = YuShuBook.keyword_url.format(keyword)
        result = HTTP.get(cls,url)
        return cls(result)