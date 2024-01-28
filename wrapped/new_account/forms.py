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
        fields = ('username', 'email', 'password1', 'password2', 'categories', )

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            categories_string = ','.join(self.cleaned_data.get('categories', []))

        # Provide default values for all UserProfile fields
            user_profile_data = {
                'categories': categories_string,
                'tearsq1': '',  # Replace with a suitable default value
                'tearsq2': '',  # Replace with a suitable default value
                'tearsq3': '',  # Repeat for all the fields
                'tearsq4': '',  # Replace with a suitable default value
                'tearsq5': '',  # Replace with a suitable default value
                'tearsq6': '',  # Replace with a suitable default value
                'partyq1': '',  # Replace with a suitable default value
                'partyq2': '',  # Replace with a suitable default value
                'partyq3': '',  # Replace with a suitable default value
                'partyq4': '',  # Replace with a suitable default value
                'partyq5': '',  # Replace with a suitable default value
                'partyq6': '',  # Replace with a suitable default value
                'date': 0,      # Replace with a suitable default value
            }

            UserProfile.objects.create(user=user, **user_profile_data)
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
