from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from new_account.models import UserProfile
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

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
                return redirect('account')
            else:
                messages.error(request, "Username or password is not correct.")
        else:
            print("Form errors:", form.errors)  # Debugging
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})

def accounts_view(request):
    # You don't need a separate query if you only need basic user info like username and email
    return render(request, 'login/account.html', {
        'username': request.user.username,
        'email': request.user.email,
        # If categories are stored in a related model, you need to fetch them
        # Example: 'categories': request.user.profile.categories
    })


def success_view(request):
    return render(request, 'login/success_page.html')

def accounts_view(request):
    return render(request, 'login/account.html')
