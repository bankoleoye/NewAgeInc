from certifi import contents
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, RegisterUserSerializer, LoginSerializer

from.models import User
from .config import onesignal_app_id, onesignal_rest_api_key

import requests
# from onesignal import OneSignal, SegmentNotification
from onesignal_sdk.client import Client

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer
    def post(self, request):
        try:
            user = request.data
            serializer = self.serializer_class(data=user)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user_data = serializer.data
            user = User.objects.get(email = user_data['email'])
        except Exception as e:
            return Response(serializer.data, status = status.HTTP_201_CREATED)

class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        if email is None or password is None:
            return Response(errors={'invalid_credentials': 'please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=email, password=password)
        if not user:
            return Response({"message": 'invalid credentials: Ensure both email and password are correct and you have verified your account'}, status=status.HTTP_400_BAD_REQUEST),
        if not user.is_verified:
            return Response({"message": 'invalid credentials: Please verify your account'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(user)
        token, _= Token.objects.get_or_create(user=user)
        return Response(data={'token': token.key}, status = status.HTTP_200_OK)


class Logout(generics.GenericAPIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

# class Delete(generics.GenericAPIView):
#     def selete()


