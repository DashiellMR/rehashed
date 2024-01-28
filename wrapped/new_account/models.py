from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categories = models.CharField(max_length=255, blank=True)  # Stores categories as a comma-separated string
    tearsq1 = models.IntegerField()
    tearsq2 = models.IntegerField()
    tearsq3 = models.CharField(max_length = 100)
    tearsq4 = models.CharField(max_length = 100)
    tearsq5 = models.CharField(max_length = 100)
    tearsq6 = models.IntegerField()
    partyq1 = models.IntegerField()
    partyq2 = models.IntegerField()
    partyq3 = models.CharField(max_length = 100)
    partyq4 = models.CharField(max_length = 100)
    partyq5 = models.CharField(max_length = 100)
    partyq6 = models.IntegerField()
    date = models.IntegerField()
    def __str__(self):
        return self.user.username
