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

@login_required
def accounts_view(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)  # Adjust if UserProfile is accessed differently

    # Split categories into a list if they exist, else provide an empty list
    categories = user_profile.categories.split(',') if user_profile.categories else []
    print(categories)
    return render(request, 'login/account.html', {
        'username': user.username,
        'email': user.email,
        'categories': categories
    })


def success_view(request):
    return render(request, 'login/success_page.html')

