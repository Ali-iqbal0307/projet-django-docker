from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('api.urls')),             
    path('admin/', admin.site.urls),
    path('message/', include('api.urls')),
    path('api/', include('api.urls')),
]

