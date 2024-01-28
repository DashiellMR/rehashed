from django.contrib.auth import authenticate, login
from django.forms import ValidationError
def acc_login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        
    else: 
        raise ValidationError("Password or username are not correct.")
    