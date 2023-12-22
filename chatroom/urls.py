from django.contrib import admin
from django.urls import path
from accounts.views import register_user, login
from app.views import get_user_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register", register_user, name="register"),
    path("login", login, name="login"),
    path("api/users", get_user_list, name="get-user-list"),
]
