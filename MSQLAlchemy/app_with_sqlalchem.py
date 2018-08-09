from flask import Flask, jsonify, request
from ext import db
from users import User

from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
# # 先清除所有的表，再创建表
# with app.app_context():
#     db.drop_all()
#     db.create_all()


#插入记录
@app.route('/users', methods=['POST'])
def users():
    #form表单， .get()获取信息
    username = request.form.get('name')
    password = request.form.get('u_password')
    

    #判断是否有重复的用户
    if User.query.filter_by(name=username).count() > 0:
        print("该用户已存在，请重新输入")
        return "This user is already exise."
    else:
        user = User(name=username,u_password=password)
        #判断用户密码是否为空
        if len(password) == 0:
        # if  not password == True:
            print("请输入用户密码")
            return "please insert password"
        else:
            print('User ID:{}'.format(user.id))
            db.session.add(user)
            db.session.commit()

            #返回注册时间
            now = datetime.now()
            print(now)
            return jsonify({'id': user.id})


#查询全部记录
@app.route('/users',methods=['GET'])
def getallusers():
    user= User.query.all()
    #在终端打印
    print(user)
    #遍历user中的所有值
    for i in user:
        #字典
        d={'id':i.id,'name':i.name,'password':i.u_password}
        print(d)
    #在网页返回值
    return "ok"


#查询单条记录
@app.route('/users/<username>',methods=['GET'])
def show_user(username):
    user = User.query.filter_by(name=username).first()
    if user == None:
        print("没有此用户")
        return "user not found"
    else:   
        print(user.u_password)
        return "ok"


#删除记录
@app.route('/users/<username>',methods=['DELETE'])
def deleteuser(username):
    a = User.query.filter_by(name=username).first()

    if a == None:
        print("没有此用户")
        return "user not found"
    else:
        print(a)
        db.session.delete(a)
        db.session.commit()
        return "ok"


#更新记录
@app.route('/users/<username>',methods=['PUT'])
def putuser(username):
    data = request.form.get('username')
    
    # print(data)
    b = User.query.filter_by(name=username).first()
    # print(b)
    if data == None or b == None:
        print("没有此用户")
        return "user not found" 
    else:
        print(data)
        print(b)
        b.name = data
        db.session.commit()
        return "ok"


        



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
