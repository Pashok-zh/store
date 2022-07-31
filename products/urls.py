from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('about/', about),
    path('cats/<int:catid>/', categories),
]