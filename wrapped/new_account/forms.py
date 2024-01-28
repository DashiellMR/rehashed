from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

CATEGORY_CHOICES = [
    ('fitness', 'Fitness'),
    ('partying', 'Partying'),
    ('cooking', 'Cooking'),
    ('studying', 'Studying'),
    ('tears', 'Tears'),
    ('relationships', 'Relationships'),
    ('gaming', 'Gaming'),
]

class UserAccountForm(UserCreationForm):
    categories = forms.MultipleChoiceField(choices=CATEGORY_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'categories')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            categories_string = ','.join(self.cleaned_data.get('categories', []))
            UserProfile.objects.create(user=user, categories=categories_string)
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

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
