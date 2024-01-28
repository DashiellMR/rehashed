from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def journal_page(request):  
    return render(request, 'journal/journal.html',)