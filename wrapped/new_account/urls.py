from django.urls import path
from .views import new_account_page

urlpatterns = [
    path("", new_account_page, name='new_account'),
]