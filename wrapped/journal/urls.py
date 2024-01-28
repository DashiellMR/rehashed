from django.urls import path
from .views import journal_page, form_data

app_name = 'journal'
urlpatterns = [
    path("", journal_page, name='journal'),
    path("form_data/", form_data, name='form_data')
]