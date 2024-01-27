from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('welcome.urls')),
    path("account/", include("account.urls")),
    path("new_account/", include("new_account.urls")),
    path("wrapped/", include("wrapped.urls")),
    path("login/", include("login.urls")),
    path("journal/", include("journal.urls"))
]