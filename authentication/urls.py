from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path("log", views.login, name="login"),
    path("register/", views.register, name="register")
]
