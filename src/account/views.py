from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UserAccountForm, LoginForm
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def welcome_page(request):
    return render(request, 'account/welcome.html')

def register_account(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:login'))
        else:
            print(form.errors)  
    else:
        form = UserAccountForm()

    return render(request, 'account/register.html', {'form': form})



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
                return redirect('account:account')
            else:
                messages.error(request, "Username or password is not correct.")
        else:
            print("Form errors:", form.errors)  # Debugging
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

@login_required
def accounts_view(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)

    categories = user_profile.categories.split(',') if user_profile.categories else []
    return render(request, 'account/account.html', {
        'username': user.username,
        'email': user.email,
        'categories': categories
    })


