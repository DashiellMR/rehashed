from django.urls import path
from .views import journal_page

urlpatterns = [
    path("", journal_page, name='journal'),
]