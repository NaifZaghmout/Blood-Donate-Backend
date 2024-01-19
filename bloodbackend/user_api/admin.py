from django.contrib import admin
from .models import AppUser, PatientBlood
from Profile.models import UserProfile
# Register your models here.
admin.site.register(AppUser)
admin.site.register(PatientBlood)
admin.site.register(UserProfile)
