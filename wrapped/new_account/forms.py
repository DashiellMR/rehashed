from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import UserAccount
from django import forms

class UserAccountForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = ['username', 'password', 'email', 'phone_number']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if UserAccount.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if UserAccount.objects.filter(email=email).exists():
            raise ValidationError("Email is already in use.")
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if UserAccount.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("Phone number is already in use.")
        return phone_number