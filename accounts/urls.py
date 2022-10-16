from django.urls import path, include
from .views import register
urlpatterns = [path('', include('rest_auth.urls')),
               path('register/', register)]
