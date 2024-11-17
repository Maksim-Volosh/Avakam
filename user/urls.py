from django.urls import path

from .views import *

app_name = 'user'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
]
