"""
Validations
"""
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def validate_email(data):
    """
    Validate Email
    """
    email = data[0]["email"].strip()
    if not email:
        raise ValidationError("an email is needed")
    return True



def validate_username(data):
    """
    Validate Username
    """
    username = data["username"].strip()
    if not username:
        raise ValidationError("choose another username")
    return True

def validate_password(data):
    """
    Validate Password
    """
    password = data[0]["password"].strip()
    if not password:
        raise ValidationError("a password is needed")
    return True
