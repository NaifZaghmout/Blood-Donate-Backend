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
    email = data["email"]
    if not email:
        raise ValidationError("an email is needed")
    return True


def validate_username(data):
    """
    Validate Username
    """
    username = data["username"]
    if not username:
        raise ValidationError("choose another username")
    return True


def validate_password(data):
    """
    Validate Password
    """
    password = data["password"]
    if not password:
        raise ValidationError("a password is needed")
    return True
