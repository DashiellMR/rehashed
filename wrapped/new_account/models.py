from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categories = models.CharField(max_length=255, blank=True)  # Stores categories as a comma-separated string

    def __str__(self):
        return self.user.username
