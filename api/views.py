from django.http import JsonResponse, HttpResponse
from .models import Message





def home(request):
    return JsonResponse({"info": "Bienvenue sur l'API. Essayez /message ou /api/message"})



def get_message(request):
    message = Message.objects.first()
    return JsonResponse({"message": message.text if message else "Aucun message"})
