from django.urls import path
from .views import UserProfileUpdate, UserProfileDetail

urlpatterns = [
    path(
        'userprofile-detail/<int:user_id>/',
        UserProfileDetail.as_view(),
        name='userprofile-detail'
    ),
    path(
        'update-profile/<int:user_id>/',
        UserProfileUpdate.as_view(),
        name='userprofile-update'
    ),
]
