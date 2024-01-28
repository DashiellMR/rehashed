from django.shortcuts import render
from .forms import acc_login

# Create your views here.
def login(request):
    #if request.method == "POST":
        
    
    return render(request, 'login/login.html')