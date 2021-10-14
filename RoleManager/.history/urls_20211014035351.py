from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(('/get_new_role_data', views.get_new_role_data, "get_new_role_data")),
    path(('/create_new_role', views.create_new_role, "create_new_role")),
]
