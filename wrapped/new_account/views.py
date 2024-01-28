from django.shortcuts import render, redirect
from .forms import UserAccountForm

def register_account(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            print(form.errors)  
    else:
        form = UserAccountForm()

    return render(request, 'new_account/newaccount.html', {'form': form})



def success(request):
    return render(request, 'new_account/success.html')
