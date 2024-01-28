import phonenumbers
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from phonenumbers import PhoneNumberMatcher, NumberParseException

class UserAccountForm(UserCreationForm):
    phone_number = forms.CharField(max_length=17, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone_number')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        phone_number = self.cleaned_data['phone_number']
        if UserProfile.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Phone number is already in use.")
        if commit:
            user.save()
            UserProfile.objects.create(user=user, phone_number=self.cleaned_data['phone_number'])
        return user
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already in use.")
        return username
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number:
            try:
                number = phonenumbers.parse(phone_number, 'US')  
                if not phonenumbers.is_valid_number(number):
                    raise forms.ValidationError("Enter a valid phone number.")
            except NumberParseException:
                raise forms.ValidationError("Enter a valid phone number.")
        return phone_number
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return password2
