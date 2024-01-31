from django.urls import path, reverse_lazy
from .views import welcome_page, register_account, login_view, accounts_view
from django.contrib.auth.views import LogoutView

app_name="account"
urlpatterns = [
    path('register/', register_account, name='register'),
    path("login/", login_view, name='login'),
    path("account/", accounts_view, name='account'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('account:login')), name='logout')
]