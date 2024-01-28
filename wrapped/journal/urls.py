from django.urls import path
from .views import journal_page

app_name = 'journal'
urlpatterns = [
    path("", journal_page, name='journal'),
]