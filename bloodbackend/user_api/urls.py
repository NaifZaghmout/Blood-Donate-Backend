"""
URLs for the app
"""
from django.urls import path
from user_api import views

urlpatterns = [
    path("register", views.UserRegister.as_view(), name="register"),
    path("login", views.UserLogin.as_view(), name="login"),
    path("logout", views.UserLogout.as_view(), name="logout"),
    path("user", views.UserView.as_view(), name="user"),
    path(
        "createpatientblood/",
        views.PatientBloodCreateView.as_view(),
        name="patient_blood_create",
    ),
    path(
        "listpatients/", views.PatientBloodListView.as_view(), name="patient_blood_list"
    ),
      path(
        "delete/<int:pk>/",
        views.PatientBloodDeleteView.as_view(),
        name="patient_blood_delete",
    ),
    path(
        "resolve/<int:pk>/",
        views.PatientBloodMarkResolvedView.as_view(),
        name="patient_blood_resolve",
    ),
]