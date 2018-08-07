from ext import db

 
 
class User(db.Model):
    __tablename__ = 'runoob_tbl'


    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    u_password = db.Column(db.String(50))

    def __init__(self,name,u_password):
        self.name = name
        self.u_password = u_password
    