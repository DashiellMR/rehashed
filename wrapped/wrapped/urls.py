from django.urls import path
from .views import wrapped_page

urlpatterns = [
    path("", wrapped_page, name='wrapped_page'),
]