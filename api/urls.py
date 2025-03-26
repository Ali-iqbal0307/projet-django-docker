from django.urls import path
from . import views

urlpatterns = [
    path('toto/', views.home, name='api_home'),                
    path('message/', views.get_message, name='message'),  
]
