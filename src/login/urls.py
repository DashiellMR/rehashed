from django.urls import path, reverse_lazy
from .views import login_view, accounts_view, success_view
from django.contrib.auth.views import LogoutView

app_name = 'login'
urlpatterns = [
    path("login/", login_view, name='login'),
    path("success/", success_view, name='success_page'),
    path("account/", accounts_view, name='account'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login:login')), name='logout')
]
