from django.urls import path
from .views import wrapped_view

urlpatterns = [
    path("", wrapped_view, name='wrapped_page'),
]