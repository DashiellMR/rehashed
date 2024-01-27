from django.urls import path
from .views import account_page

urlpatterns = [
    path("", account_page, name='account'),
]