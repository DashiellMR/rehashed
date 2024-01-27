from django.shortcuts import render, redirect
from .forms import UserAccountForm


def register_account(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        print("Form received:", form.is_bound)  # Check if form is bound
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            print("Form errors:", form.errors)  # Print form errors
    else:
        form = UserAccountForm()

    return render(request, 'new_account/newaccount.html', {'form': form})

def success(request):
    return render(request, 'new_account/success.html')
