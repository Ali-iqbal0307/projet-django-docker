from django.shortcuts import render

from django.http import JsonResponse
from .models import Message

def get_message(request):
    message = Message.objects.first()
    return JsonResponse({"message": message.text if message else "Aucun message"})

def home(request):
    return JsonResponse({"info": "Bienvenue sur l'API. Essayez /message ou /api/message"})

