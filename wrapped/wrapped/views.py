from django.shortcuts import render
from new_account.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def wrapped_view(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)  # Adjust if UserProfile is accessed differently
    number = '100'
    user_profile.tearsq1 += ',' + number
    user_profile.save()
    user_tears1 = user_profile.tearsq1.split(',') if user_profile.tearsq1 else []
    user_party1 = user_profile.partyq1

    categories = user_profile.categories.split(',') if user_profile.categories else []
    return render(request, 'wrapped/wrapped.html', {
        'username': user.username,
        'email': user.email,
        'categories': categories,
        'tears': user_tears1[3],
        'party': user_party1
    })
