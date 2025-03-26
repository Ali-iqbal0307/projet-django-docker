from django.urls import path

from .views import get_message
from .views import home

urlpatterns = [
    path('', home),
    path('message/', get_message),
]
