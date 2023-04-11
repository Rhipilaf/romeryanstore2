import copy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Polzovatel
from shop.serializer import LoginSerializer, RegistrationSerializer, PolzovatelPhotoSerializer


class Login(APIView):

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                polzovatel = Polzovatel.objects.get(nickname=serializer.data["nickname_mail"])
                user = authenticate(request, username=polzovatel.user.username, password=serializer.data["parol"])
            except Exception:
                try:
                    polzovatel = Polzovatel.objects.get(mail=serializer.data["nickname_mail"])
                    user = authenticate(request, username=polzovatel.user.username, password=serializer.data["parol"])
                except Exception:
                    try:
                        user = authenticate(request, username=serializer.data["nickname_mail"],
                                            password=serializer.data["parol"])
                    except Exception:
                        return Response({'text': 'Ошибка авторизации'}, status=status.HTTP_400_BAD_REQUEST)

            if user is not None:
                login(request, user)
                return Response({}, status=200)

            return Response({'text': 'Ошибка авторизации'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    def get(self, request):
        logout(request)
        return redirect('/')


class Registration(APIView):
    def post(self, request):

        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():

            if len(request.data['parol']) < 8:
                return Response({'text': 'В пароле должно быть 8 или более символов'},
                                status=status.HTTP_400_BAD_REQUEST)

            if Polzovatel.objects.filter(mail=request.data['mail']).count() != 0:
                return Response({'text': 'Пользователь с такой электронной почтой уже существует'},
                                status=status.HTTP_400_BAD_REQUEST)

            if Polzovatel.objects.filter(nickname=request.data['nickname']).count() != 0:
                return Response({'text': 'Пользователь с таким никнеймом уже существует'},
                                status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(request.data['nickname'], request.data['mail'], request.data['parol'])
            Polzovatel.objects.create(
                nickname=request.data['nickname'],
                mail=request.data['mail'],
                user=user)
            login(request, user)

            return Response({'text': 'Регистрация прошла успешно'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PolzovatelChangePhoto(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):

        serializer = PolzovatelPhotoSerializer(request.user.polzovatel, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)