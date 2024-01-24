from django.shortcuts import render
# views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404


class UserProfileUpdate(APIView):
    """
    Update User Profile
    """
    permission_classes = (permissions.AllowAny,)
    # permission_classes = (IsAuthenticated,)

    def put(self, request, user_id):
        # Assuming you have an authentication system and permissions in place

        try:
            user_profile = UserProfile.objects.get(user_id=user_id)
        except UserProfile.DoesNotExist:
            return Response({
                'error': 'User Profile not found.'},
                 status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(user_profile, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileDetail(APIView):
    """
    Retrieve User Profile by user ID
    """
    permission_classes = (permissions.AllowAny,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        user_profile = get_object_or_404(UserProfile, user_id=user_id)
        serializer = UserProfileSerializer(user_profile, context={
            'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
