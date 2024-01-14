from django.contrib import admin
from .models import AppUser, PatientBlood
# Register your models here.
admin.site.register(AppUser)
admin.site.register(PatientBlood)
