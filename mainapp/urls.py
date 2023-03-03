from django.urls import path

from . import views

urlpatterns = [
    path('', views.VIEW_index, name="index"),
]