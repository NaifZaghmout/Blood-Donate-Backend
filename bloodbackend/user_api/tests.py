from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from user_api.models import AppUser
from .models import PatientBlood
from .serializers import PatientBloodSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

class PatientBloodTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = AppUser.objects.create_user(email='testuser@example.com', username='testuser', password='testpassword')

    def create_patient_blood(self, **kwargs):
        defaults = {
            'patient_name': 'Test Patient',
            'patient_email': 'test@example.com',
            'patient_phone_number': '1234567890',
            'patient_blood_type': 'A+',
            'patient_health_information': 'Test health info',
            'resolved': False,
        }
        defaults.update(kwargs)
        return PatientBlood.objects.create(**defaults)

    def test_create_patient_blood(self):
        url = '/api/createpatientblood/'
        data = {
            'patient_name': 'Test Patient',
            'patient_email': 'test@example.com',
            'patient_phone_number': '1234567890',
            'patient_blood_type': 'A+',
            'patient_health_information': 'Test health info',
            'resolved': False,
        }

        self.client.force_login(self.user)

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PatientBlood.objects.count(), 1)
        self.assertEqual(PatientBlood.objects.get().patient_name, 'Test Patient')

    def test_list_patient_blood(self):
        self.create_patient_blood()  # Create a patient blood record for testing
        url = '/api/listpatients/'

        self.client.force_login(self.user)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), PatientBlood.objects.count())

    def test_delete_patient_blood(self):
        patient_blood = self.create_patient_blood()
        url = f'/api/delete/{patient_blood.id}/'

        self.client.force_login(self.user)

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PatientBlood.objects.count(), 0)

    def test_mark_resolved_patient_blood(self):
        patient_blood = self.create_patient_blood()
        url = f'/api/resolve/{patient_blood.id}/'
        data = {'resolved': True}

        self.client.force_login(self.user)

        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

#register test case
class UserRegisterTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_register(self):
        url = f'/api/register'  # Assuming 'register' is the name of your URL pattern
        data = {
            'username': 'ztestuser',
            'email': 'ztestuser@example.com',
            'password': 'testpassword',
            'password2': 'testpassword',
        }

        response = self.client.post(url, data, format='json')
        print(response.content) 

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertTrue(AppUser.objects.filter(username='ztestuser').exists())

    def test_user_register_duplicate_username(self):
        AppUser.objects.create_user(username='ztestuser', email='existing@example.com', password='existingpassword')

        url = f'/api/register' 
        data = {
            'username': 'ztestuser', 
            'email': 'ztestuser@example.com',
            'password': 'testpassword',
            'password2': 'testpassword',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Username already exists.', str(response.data))

    def test_user_register_duplicate_email(self):
        AppUser.objects.create_user(username='existinguser', email='testuser@example.com', password='existingpassword')

        url = f'/api/register'  
        data = {
            'username': 'ztestuser',
            'email': 'testuser@example.com', 
            'password': 'testpassword',
            'password2': 'testpassword',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Email already exists.', str(response.data))

class UserLoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'ztestuser',
            'email': 'ztestuser@example.com',
            'password': 'testpassword',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.login_url = reverse('login') 

    def test_user_login(self):
       
        data = {
            'email': 'ztestuser@example.com',
            'password': 'testpassword',
            'username': 'ztestuser',
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data.get('data').get('username'), 'ztestuser')



     