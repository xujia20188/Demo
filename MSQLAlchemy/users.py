from ext import db
from datetime import datetime
 
 
class User(db.Model):
    __tablename__ = 'runoob_tbl'


    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),unique=True,nullable=False)
    u_password = db.Column(db.String(50),nullable=False)
    #时间模块
    time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self,name,u_password):
        self.name = name
        self.u_password = u_password
    