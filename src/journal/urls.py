from django.urls import path
from .views import journal_page, form_data, wrapped_view

app_name = 'journal'
urlpatterns = [
    path("", journal_page, name='journal'),
    path("form_data/", form_data, name='form_data'),
    path("wrapped/", wrapped_view, name='wrapped')
]