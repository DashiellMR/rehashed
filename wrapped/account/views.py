from django.shortcuts import render

# Create your views here.
 def account_page(request):
     return render(request, 'account/account.html')