from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(('/create_new_role', views.create_new_role, name="create_new_role"))
]
