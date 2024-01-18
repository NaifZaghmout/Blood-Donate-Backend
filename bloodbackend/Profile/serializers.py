import email
from rest_framework import serializers
from .models import AppUser, UserProfile
from user_api.serializers import UserLoginSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    email = serializers.SerializerMethodField('get_email')

    class Meta:
        model = UserProfile
        fields = ('user','staff_id', 'avatar', 'bio','username','email')

    
    def get_username(self,obj):
        if obj:
            username = obj.user.username
            return username
        return None
    
    def get_email(self,obj):
        if obj:
            email = obj.user.email
            return email
        return None

 

   