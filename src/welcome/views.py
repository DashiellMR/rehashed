from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserAccountForm

def welcome_page(request):
    return render(request, 'welcome/welcome.html')

def register_account(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login:login'))
        else:
            print(form.errors)  
    else:
        form = UserAccountForm()

    return render(request, 'welcome/newaccount.html', {'form': form})


def success(request):
    return render(request, 'welcome/success.html')
