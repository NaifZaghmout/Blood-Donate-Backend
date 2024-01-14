"""
Django App Serializers
"""
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
from .models import PatientBlood, AppUser

UserModel = AppUser


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    User Register
    """

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'password2']

    def create(self, validated_data):
        password = validated_data['password']
        password2 = validated_data.get('password2')
        if password != password2:
            raise serializers.ValidationError
            ({'password': 'Passwords must match.'})
        user_data = dict(validated_data)
        user_data.pop('password2', None)

        user = UserModel.objects.create_user(**user_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    """
    User Login
    """
    email = serializers.EmailField()
    password = serializers.CharField()
    username = serializers.CharField()

    class Meta:
        model = UserModel
        fields = ['email', 'password', 'username']

    def validate(self, data):
        username = data['username']
        user = authenticate(
         request=self.context.get('request'),
         email=data['email'],
         password=data['password']
        )
    if user and user.is_active:
        if username and user.username != username:
            raise serializers.ValidationError(
                "Invalid credentials - Username does not match."
            )
        return user
    raise serializers.ValidationError("Email or Password is incorrect.")


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
