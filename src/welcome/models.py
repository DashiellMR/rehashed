from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categories = models.CharField(max_length=255, blank=True)
    tearsq1 = models.CharField(max_length=800, blank=True, null=True)
    tearsq2 = models.CharField(max_length=800, blank=True, null=True)
    tearsq3 = models.CharField(max_length=800, blank=True, null=True)
    tearsq4 = models.CharField(max_length=800, blank=True, null=True)
    tearsq5 = models.CharField(max_length=800, blank=True, null=True)
    tearsq6 = models.CharField(max_length=800, blank=True, null=True)
    partyq1 = models.CharField(max_length=800, blank=True, null=True)
    partyq2 = models.CharField(max_length=800, blank=True, null=True)
    partyq3 = models.CharField(max_length=800, blank=True, null=True)
    partyq4 = models.CharField(max_length=800, blank=True, null=True)
    gamingq1 = models.CharField(max_length=800, blank=True, null=True)
    gamingq2 = models.CharField(max_length=800, blank=True, null=True)

    def __str__(self):
        return self.user.username

