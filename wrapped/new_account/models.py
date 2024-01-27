from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    # Categories can be stored as a ManyToManyField if they are a separate model,
    # or as a TextField with comma-separated values, depending on your design