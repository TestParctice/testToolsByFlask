from flask import render_template
from . import app_message


@app_message.route('/get_message')
def get_message():
    return render_template('message.html', message='123123')
