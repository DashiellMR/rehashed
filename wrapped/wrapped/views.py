from django.shortcuts import render
from new_account.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def wrapped_page(request):
    # No context is passed for now, but you can add context data if needed
    return render(request, 'wrapped/wrapped.html')

@login_required
def wrapped_view(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)  # Adjust if UserProfile is accessed differently

    # Split categories into a list if they exist, else provide an empty list
    categories = user_profile.categories.split(',') if user_profile.categories else []
    print(categories)
    return render(request, '/wrapped/wrapped.html', {
        'username': user.username,
        'email': user.email,
        'categories': categories
    })