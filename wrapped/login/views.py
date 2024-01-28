from django.shortcuts import render
from .forms import acc_login

# Create your views here.
def login_page(request):
    return render(request, 'login/login.html')