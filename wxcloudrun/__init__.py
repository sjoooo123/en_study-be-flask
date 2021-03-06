from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql
import config

# 因MySQLDB不支持Python3，使用pymysql扩展库代替MySQLDB库
pymysql.install_as_MySQLdb()

# 初始化web应用
app = Flask(__name__, instance_relative_config=True)
CORS(app)

app.config['DEBUG'] = config.DEBUG

# 设定数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/flask_demo'.format(config.username, config.password,
                                                                             config.db_address)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 初始化DB操作对象
db = SQLAlchemy(app)

# 加载控制器
if True:
    from wxcloudrun.counters import views
    from wxcloudrun.category import views
    from wxcloudrun.prefix import views
    from wxcloudrun.suffix import views
    from wxcloudrun.wordroot import views
    from wxcloudrun.common import views

# 加载配置
app.config.from_object('config')
