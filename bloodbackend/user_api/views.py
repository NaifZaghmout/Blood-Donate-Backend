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
from .models import PatientBlood,AppUser
from rest_framework import permissions, status, generics
from .validations import  validate_email, validate_password
import logging
from django.core.exceptions import ValidationError




logger = logging.getLogger(__name__)


class UserRegister(APIView):
    """
    User Register
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request):

        
        try:
            clean_data = request.data
            if AppUser.objects.filter(username=clean_data['username']).exists():
                return Response({'error':'Username already exists.'},status=status.HTTP_400_BAD_REQUEST)
            if AppUser.objects.filter(email=clean_data['email']).exists():
                return Response({'error':'Email already exists.'},status=status.HTTP_400_BAD_REQUEST)
            serializer = UserRegisterSerializer(data=clean_data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.create(clean_data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ve:
            return Response({"detail": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserLogin(APIView):
    """
    User Login
    """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            login(request, user)
            response_data = serializer.data.copy()
            response_data.pop('password')
            return Response({'data':response_data}, status=status.HTTP_200_OK)




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

    permission_classes = [permissions.AllowAny]

    queryset = PatientBlood.objects.all()
    serializer_class = PatientBloodSerializer




    
class PatientBloodDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = PatientBlood.objects.all()
    serializer_class = PatientBloodSerializer
    



class PatientBloodMarkResolvedView(generics.UpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = PatientBlood.objects.all()
    serializer_class = PatientBloodSerializer

    def update(self, request, *args, **kwargs):
        """
        Update the case as resolved
        """
        instance = self.get_object()
        instance.mark_as_resolved()
        serializer = PatientBloodSerializer(instance,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)




class PatientBloodUnresolvedListView(generics.ListAPIView):
    serializer_class = PatientBloodSerializer

    def get_queryset(self):
        return PatientBlood.objects.filter(resolved=False)




class PatientBloodDetailView(generics.RetrieveAPIView):
    """
    Retrieve details for a specific PatientBlood instance.
    """
    permission_classes = [permissions.AllowAny]
    queryset = PatientBlood.objects.all()
    serializer_class = PatientBloodSerializer
    lookup_field = 'id' 




class CheckUserLoggedIn(APIView):
    """
    Check if the user is logged in.
    """    
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        """
        Get method to check user login status.
        """
        username = request.data.get('username','')
       
        user = AppUser.objects.filter(username=username).first()
        user_status = {
            'is_authenticated':user.is_authenticated,
        }
   
        return Response({'message': user_status}, status=status.HTTP_200_OK)
        

