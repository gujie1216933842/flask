from flask import Flask
from flask import request
import platform
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Hello flask</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In </button></p>
    </form>
    '''


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello ,admin!</h3>'
    return '<h3>Bad username or password</h3>'


if __name__ == '__main__':
    operation = platform.platform()
    if 'Linux' in operation:
        app.run(host="0.0.0.0",port='5000')
    else:
        app.run()
