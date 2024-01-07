from django.urls import path


from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", views.login_view, name="auth_login"),
    path("register/", views.register_view, name="register_view"),
]
