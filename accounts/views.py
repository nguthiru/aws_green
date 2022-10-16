import imp
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

USERS = get_user_model()
# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get("username")
    password1 = request.data.get("password1")
    password2 = request.data.get("password2")
    email = request.data.get("email")

    if (username == None or password1 == None or password2 == None or email == None):
        return Response("Fill all fields", status=400)
    if password1 != password2:
        return Response("Passwords don't match", status=400)
    else:
        try:
            user = USERS.objects.get(username=username)
            return Response("User already exists", status=400)
        except USERS.DoesNotExist:
            user = USERS.objects.create(username=username, email=email)
            user.set_password(password1)
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({"token": token.key,}, status=201)