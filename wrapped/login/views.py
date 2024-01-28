from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("POST data:", request.POST)  # Debugging

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            print("User authenticated:", user is not None)  # Debugging

            if user is not None:
                login(request, user)
                return redirect('success_page')
            else:
                messages.error(request, "Username or password is not correct.")
        else:
            print("Form errors:", form.errors)  # Debugging
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})

def success_view(request):
    return render(request, 'login/success_page.html')
