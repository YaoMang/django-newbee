from django.urls import path

from . import views

app_name = 'userauth'
urlpatterns = [
    path('', views.VIEW_index, name="index"),
    path('signin/', views.login, name="signin"),
    path('signup/', views.VIEW_signup, name="signup"),
]