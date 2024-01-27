from django.shortcuts import render

# Create your views here.
def journal_page(request):
    return render(request, 'journal/journal.html')