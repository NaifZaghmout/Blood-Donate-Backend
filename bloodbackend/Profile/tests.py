from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from user_api.models import AppUser
from .models import UserProfile


class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = AppUser.objects.create(username='testuser', email='test@example.com', password='testpassword')

    def tearDown(self):
        self.user.delete()

    def test_user_profile_creation(self):

        profile = UserProfile.objects.create(
            user=self.user,
            staff_id='STAFF-1234',
            avatar=SimpleUploadedFile(
                "test_avatar.jpg", b"file_content", content_type="image/jpeg"),
            bio='Test bio content'
        )

        self.assertEqual(UserProfile.objects.count(), 1)

        self.assertTrue(profile.staff_id.startswith('STAFF-'))

        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.avatar.name, 'avatars/test_avatar.jpg')
        self.assertEqual(profile.bio, 'Test bio content')

    def test_generate_staff_id(self):

        staff_id = UserProfile.generate_staff_id()

        self.assertTrue(staff_id.startswith('STAFF-'))

        self.assertRegex(staff_id, r'STAFF-\d{4}')

    def test_user_profile_str_method(self):

        profile = UserProfile.objects.create(
            user=self.user, staff_id='STAFF-5678')

        self.assertEqual(str(profile), 'testuser - STAFF-5678')
