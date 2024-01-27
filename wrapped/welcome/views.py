from django.shortcuts import render

def welcome_page(request):
    # No context is passed for now, but you can add context data if needed
    return render(request, 'welcome/welcome.html')