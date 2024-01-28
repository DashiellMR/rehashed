from django.shortcuts import render
from new_account.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def journal_page(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)  # Adjust if UserProfile is accessed differently
    
    
    categories = user_profile.categories.split(',') if user_profile.categories else []
    return render(request, 'journal/journal.html', {
        'username': user.username,
        'email': user.email,
        'categories': categories
    })
