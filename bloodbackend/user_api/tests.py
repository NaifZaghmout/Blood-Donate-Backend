from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from user_api.models import AppUser
from .models import PatientBlood
from .serializers import PatientBloodSerializer

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
        self.assertTrue(PatientBlood.objects.get(id=patient_blood.id).resolved)


     