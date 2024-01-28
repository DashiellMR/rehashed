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
        
        # Assign the form data values to the appropriate fields of the UserProfile instance
        user_profile.tearsq1 = cry_times
        user_profile.tearsq2 = total_cry_time
        user_profile.tearsq3 = cry_location
        user_profile.tearsq4 = cry_reason
        user_profile.tearsq5 = cry_intensity
        user_profile.tearsq6 = watched_you_cry
        user_profile.partyq1 = party_cry_times
        user_profile.partyq2 = party_total_drinks
        user_profile.partyq3 = party_location
        user_profile.partyq4 = party_reason
        
        # Save the UserProfile instance to the database
        user_profile.save()
        
        # You can redirect the user to another page after saving the data
        return redirect('login:account')  # Replace 'some_success_page' with the actual URL