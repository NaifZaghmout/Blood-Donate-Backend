"""
Django App Serializers
"""
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
from .models import PatientBlood

UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    User Register
    """
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, clean_data):
        """
        Create
        """
        user_obj = UserModel.objects.create_user(
            email=clean_data["email"], password=clean_data["password"]
        )
        user_obj.username = clean_data["username"]
        user_obj.save()
        return user_obj

class UserLoginSerializer(serializers.Serializer):
    """
    User Login
    """
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        """
        Create User
        """
        user = authenticate(
            username=clean_data["email"], password=clean_data["password"]
        )
        if not user:
            raise ValidationError("user not found")
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("email", "username")

class PatientBloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientBlood
        fields = [
            "id",
            "patient_name",
            "patient_email",
            "patient_phone_number",
            "patient_blood_type",
            "patient_health_information",
        ]
