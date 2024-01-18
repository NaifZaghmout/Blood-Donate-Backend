from django.db import models
from user_api.models import AppUser

# Create your models here.
class UserProfile(models.Model):
    """
    User Profile
    """
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='user_profile')
    staff_id = models.CharField(max_length=20,null=True,blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.staff_id}"
    
    @staticmethod
    def generate_staff_id():
        import random
        return f'STAFF-{random.randint(1000, 9999)}'
    

   
