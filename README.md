# testToolsByFlask
使用时需要在testToolsByFlask下增加config.cfg文件,用来保存配置信息
例如：
config.cfg:
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql://***:***@0.0.0.0:3306/***'
SQLALCHEMY_COMMIT_ON_TEARDOWN = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True