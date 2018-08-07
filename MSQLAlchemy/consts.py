# 固定常量


DIALECT = 'mysql'
DRIVE = 'pymysql'
USERNAME = 'root'
PASSWORD = '123'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'dev'
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=UTF8MB4".format(
    DIALECT, DRIVE, USERNAME, PASSWORD, HOST, PORT, DATABASE)
