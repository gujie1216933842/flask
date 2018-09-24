from . import web
from flask import render_template
from app.forms.auth import RegisterForm
from app.models.user import User
from app.models.base import db


@web.route('/register')
def register(request):
    form = RegisterForm()  # 构建了一个验证form,当请求type是post的时候,才校验
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attr(form.data)
        db.session.add(user)
        db.session.commit()
    return render_template('auth/register.html', form={'data:{}'})


@web.route('/login', method=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', method=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', method=['GET', 'POST'])
def forget_password(token):
    pass
