from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None



class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if 'username' in kwargs:
            username = kwargs.get('username')
        if username is None or password is None:
            return None
        try:
            if is_valid_email(username):
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
