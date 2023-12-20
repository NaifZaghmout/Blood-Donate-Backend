"""
Views for the app
"""
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserSerializer,
    PatientBloodSerializer,)
from .models import PatientBlood
from rest_framework import permissions, status, generics
from .validations import custom_validation, validate_email, validate_password




class UserRegister(APIView):
    """
    User Register
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        """
        Post
        """
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)



class UserLogin(APIView):
    """
    User Login
    """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    
    def post(self, request):
        """
        Post
        """
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)




class UserLogout(APIView):
    """
    User Logout
    """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        """
        Post
        """
        logout(request)
        return Response(status=status.HTTP_200_OK)




class UserView(APIView):
    """
    User View
    """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)



class PatientBloodCreateView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = PatientBloodSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PatientBloodListView(generics.ListAPIView):
    queryset = PatientBlood.objects.all()
    serializer_class = PatientBloodSerializer




    
class PatientBloodDeleteView(generics.DestroyAPIView):
    queryset = PatientBlood.objects.all()
    serializer_class = PatientBloodSerializer
    lookup_field = "id"




class PatientBloodMarkResolvedView(generics.UpdateAPIView):
    queryset = PatientBlood.objects.all()
    serializer_class = PatientBloodSerializer
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        """
        Update the case as resolved
        """
        instance = self.get_object()
        instance.mark_as_resolved()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)




class PatientBloodUnresolvedListView(generics.ListAPIView):
    serializer_class = PatientBloodSerializer

    def get_queryset(self):
        return PatientBlood.objects.filter(resolved=False)
        

