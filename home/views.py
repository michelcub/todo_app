from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home_view(request):
    return render(request, 'views/home.html', {})


def login_view(request):
    return render(request, 'auth/login.html', {})

def register_view(request):
    return render(request, 'auth/register.html', {})