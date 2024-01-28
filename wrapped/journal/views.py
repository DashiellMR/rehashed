from django.shortcuts import render
from new_account.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404

@login_required
def journal_page(request):
    user = request.user
    
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=user)
        user_profile.save()
    
    categories = user_profile.categories.split(',') if user_profile.categories else []
    
    return render(request, 'journal/journal.html', {
        'username': user.username,
        'email': user.email,
        'categories': categories
    })

def form_data(request):
    if request.method == "POST":
        cry_times = request.POST.get("cry_times")
        total_cry_time = request.POST.get("total_cry_time")
        cry_location = request.POST.get("cry_location")
        cry_reason = request.POST.get("cry_reason")
        cry_intensity = request.POST.get("cry_intensity")
        watched_you_cry = request.POST.get("watched_you_cry")
        
        party_cry_times = request.POST.get("party_cry_times")
        party_total_drinks = request.POST.get("party_total_drinks")
        party_location = request.POST.get("party_location")
        party_reason = request.POST.get("party_reason")
        # Get the logged-in user
        user = request.user
        
        # Create an instance of UserProfile associated with the user
        user_profile = UserProfile.objects.get(user=user)  # Adjust if UserProfile is accessed differently
        
        user_profile.tearsq1 = user_profile.tearsq1 + "," + cry_times if user_profile.tearsq1 else cry_times
        user_profile.tearsq2 = user_profile.tearsq2 + "," + total_cry_time if user_profile.tearsq2 else total_cry_time
        user_profile.tearsq3 = user_profile.tearsq3 + "," + cry_location if user_profile.tearsq3 else cry_location
        user_profile.tearsq4 = user_profile.tearsq4 + "," + cry_reason if user_profile.tearsq4 else cry_reason
        user_profile.tearsq5 = user_profile.tearsq5 + "," + cry_intensity if user_profile.tearsq5 else cry_intensity
        user_profile.tearsq6 = user_profile.tearsq6 + "," + watched_you_cry if user_profile.tearsq6 else watched_you_cry
        
        # Update "Partying" section fields by appending new values
        user_profile.partyq1 = user_profile.partyq1 + "," + party_cry_times if user_profile.partyq1 else party_cry_times
        user_profile.partyq2 = user_profile.partyq2 + "," + party_total_drinks if user_profile.partyq2 else party_total_drinks
        user_profile.partyq3 = user_profile.partyq3 + "," + party_location if user_profile.partyq3 else party_location
        user_profile.partyq4 = user_profile.partyq4 + "," + party_reason if user_profile.partyq4 else party_reason
        
        # Save the UserProfile instance to the database
        user_profile.save()
        
        # You can redirect the user to another page after saving the data
        return redirect('login:account')  # Replace 'some_success_page' with the actual URL