from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Yury'}
    return render_template('index.html', title='Home sweet home', user=user)
