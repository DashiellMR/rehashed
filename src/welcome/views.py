from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UserAccountForm, LoginForm
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def welcome_page(request):
    return render(request, 'welcome/welcome.html')

def register_account(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login:login'))
        else:
            print(form.errors)  
    else:
        form = UserAccountForm()

    return render(request, 'welcome/newaccount.html', {'form': form})



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
                return redirect('welcome:account')
            else:
                messages.error(request, "Username or password is not correct.")
        else:
            print("Form errors:", form.errors)  # Debugging
    else:
        form = LoginForm()

    return render(request, 'welcome/login.html', {'form': form})

@login_required
def accounts_view(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)

    categories = user_profile.categories.split(',') if user_profile.categories else []
    return render(request, 'welcome/account.html', {
        'username': user.username,
        'email': user.email,
        'categories': categories
    })


