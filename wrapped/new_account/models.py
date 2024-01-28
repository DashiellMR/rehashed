from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categories = models.CharField(max_length=255, blank=True)  # Stores categories as a comma-separated string
    tearsq1 = models.CharField(max_length = 800)
    tearsq2 = models.CharField(max_length = 800)
    tearsq3 = models.CharField(max_length = 800)
    tearsq4 = models.CharField(max_length = 800)
    tearsq5 = models.CharField(max_length = 800)
    tearsq6 = models.CharField(max_length = 800)
    partyq1 = models.CharField(max_length = 800)
    partyq2 = models.CharField(max_length = 800)
    partyq3 = models.CharField(max_length = 800)
    partyq4 = models.CharField(max_length = 800)
    partyq5 = models.CharField(max_length = 800)
    partyq6 = models.CharField(max_length = 800)
    date = models.IntegerField()
    def __str__(self):
        return self.user.username
