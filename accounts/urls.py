from django.urls import path
from .views import register,custom_login
from . import views

urlpatterns = [
    path('register/',views.register,name = 'register'),
    path('login/',views.custom_login, name="login")
]