"""
Database models
"""
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

class AppUserManager(BaseUserManager):
    """
    User management
    """

    def create_user(self, email, password=None):
        """
        Create the user
        """
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        """
        Create the super user
        """
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()
        return user
