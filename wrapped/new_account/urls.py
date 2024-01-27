from django.urls import path
from .views import register_account, success


urlpatterns = [
    path('register/', register_account, name='register'),
    path('success/', success, name='success')
]