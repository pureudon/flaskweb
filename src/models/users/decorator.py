from functools import wraps
from flask import session
from flask import url_for
from flask import redirect
from flask import request
from src.app import app


# def requires_login(func):
#     @wraps(func)
#     def decorated_function():
#         print("Hi")
#         return func()
#     return decorated_function
#
# @requires_login
# def my_function():
#     print("hello world")
#     return "Hi"
#
# my_function()

def requires_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next=request.path))
        return func(*args, **kwargs)
    return decorated_function

# @requires_login
# def my_function(x, y):
#     return x+y
#
# my_function(5, 6)


def requires_admin_permissions(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next=request.path))
        if session['email'] not in app.config['ADMINS']:
            return redirect(url_for('users.login_user'))
        return func(*args, **kwargs)
    return decorated_function
