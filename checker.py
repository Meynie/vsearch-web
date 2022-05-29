from flask import session

from functools import wraps


def check_logged_in(func) -> str:
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func()
        return 'You are not logged in'
    return wrapper
