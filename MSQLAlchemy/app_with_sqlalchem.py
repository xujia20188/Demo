from flask import Flask, jsonify, request

from ext import db
from users import User

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
# 先清除所有的表，再创建表
# with app.app_context():
#     db.drop_all()
#     db.create_all()


@app.route('/users', methods=['POST'])
def users():
    username = request.form.get('name')
    password = request.form.get('u_password')
    user = User(name=username,u_password=password)
    

    print('User ID:{}'.format(user.id))
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id})


@app.route('/users',methods=['GET'])
def getallusers():
    user= User.query.all()
    # print(user)
    for i in user:
        d={'id':i.id,'name':i.name,'password':i.u_password}
        print(d)
    return "ok"

@app.route('/users/<username>',methods=['GET'])
def show_user(username):
    user = User.query.filter_by(name=username).first_or_404()
    print(user.u_password)
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
