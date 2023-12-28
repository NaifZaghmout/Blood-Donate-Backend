"""
Validations
"""
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def custom_validation(data):
    """
    Cusotom Validation
    """

    email = data["email"].strip()
    username = data["username"].strip()
    password = data["password"].strip()
    confirm_password = data["password2"].strip()

    if not email:
        raise ValidationError("Email is required.")
    if UserModel.objects.filter(email=email).exists():
        raise ValidationError("Email already in use.")

    if not password:
        raise ValidationError("Password is required.")
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    
    if password != confirm_password:
        raise ValidationError("Passwords do not match.")

    if not username:
        raise ValidationError("Username is required.")

    return data

def validate_email(data):
    """
    Validate Email
    """
    email = data["email"].strip()
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
    password = data["password"].strip()
    if not password:
        raise ValidationError("a password is needed")
    return True
