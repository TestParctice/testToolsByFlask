from flask import Flask
from message import app_message
from flask_script import Manager

app = Flask(__name__)
app.register_blueprint(app_message, url_prefix='/message')
manager = Manager(app)

# 使用配置文件
app.config.from_pyfile("config.cfg")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
    # app.run(host='0.0.0.0', port=80, debug=True)
