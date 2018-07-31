#地址     http://t.yushu.im/v2/book/isbn/9787501524044


from urllib import request
import requests

class HTTP:
    @staticmethod
    def get(self,url,return_json=True):
        r =requests.get(url)
        if r.status_code !=200:
            #python三元表达式
            return {} if return_json else ''
        return r.json() if return_json else r.text



        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()   #json序列化
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return{}
        #     else:
        #         return ''
