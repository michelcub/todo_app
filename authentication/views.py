from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
# Create your views here.


    
@require_POST
def login(request):
    if request.method == 'POST':
        print(request.POST.get('email'))
        print(request.POST.get('password'))
        return redirect('home')
    
    return redirect('home')
    

    

def register(request):
    print('hello')
    if request.method == 'POST':
        return redirect('home')