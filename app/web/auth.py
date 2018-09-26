from . import web
from flask import render_template, request
from app.forms.auth import RegisterForm
from app.models.user import User
from app.models.base import db


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)  # 构建了一个验证form,当请求type是post的时候,才校验

    print(request.method)
    #
    print(form.validate())

    if request.method == 'POST' and not form.validate():
        # print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')

        user = User()
        user.set_attr(form.data)
        db.session.add(user)
        db.session.commit()
    return render_template('auth/register.html', form={'data': {}})


@web.route('/login', methods=['GET', 'POST'])
def login(request):
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request(request):
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass
