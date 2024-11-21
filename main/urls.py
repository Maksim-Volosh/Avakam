from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('search/', listing_found, name='listing_found'),
    path('search/not_found/', listing_not_found, name='listing_not_found'),
]
