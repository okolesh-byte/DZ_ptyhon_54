from django.contrib import admin
from django.urls import path

from password import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("password/", views.password, name="password"),
]
