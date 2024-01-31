from django.urls import path, reverse_lazy
from .views import welcome_page, register_account, success, login_view, accounts_view, success_view
from django.contrib.auth.views import LogoutView

app_name="welcome"
urlpatterns = [
    path("", welcome_page, name='welcome'),
    path('register/', register_account, name='register'),
    path('success/', success, name='success'),
    path("login/", login_view, name='login'),
    path("success/", success_view, name='success_page'),
    path("account/", accounts_view, name='account'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('welcome:login')), name='logout')
]