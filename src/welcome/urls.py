from django.urls import path
from .views import welcome_page, register_account, success

app_name="welcome"
urlpatterns = [
    path("", welcome_page, name='welcome'),
    path('register/', register_account, name='register'),
    path('success/', success, name='success')
]