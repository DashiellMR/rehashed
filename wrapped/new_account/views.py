from django.shortcuts import render, redirect
from .forms import UserAccountForm

def register_account(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the 'account' view in the 'login' app
            return redirect('login:/login/account')  # Use 'login:account' if namespaced
        else:
            print(form.errors)  
    else:
        form = UserAccountForm()

    return render(request, 'new_account/newaccount.html', {'form': form})


def success(request):
    return render(request, 'new_account/success.html')
