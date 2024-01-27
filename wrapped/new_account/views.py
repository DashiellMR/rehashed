from django.shortcuts import render

# Create your views here.
def new_account_page(request):
    return render(request, 'new_account/newaccount.html')