from django.shortcuts import render

def wrapped_page(request):
    # No context is passed for now, but you can add context data if needed
    return render(request, 'wrapped/wrapped.html')