from . import views
from user import views as user_views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns=[
    path("", views.home, name="home"),
    path("Registration/", user_views.registration, name="registration"),
    path ("Login/", auth_views.LoginView.as_view(template_name="user/login.html"), name="login")
]
