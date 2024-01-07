from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path("user/", include('user.urls')),
    path("auth/", include('authentication.urls')),
    
]
