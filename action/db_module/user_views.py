from email.headerregistry import Address
from http.client import HTTPResponse
from json import JSONDecodeError
from operator import contains
import re
from sqlite3 import IntegrityError
from traceback import print_tb
from urllib.parse import uses_relative
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import UserProfile, Contacts, Event
from .serializers import ContactsSerializer, EventSerializer


class CreateUser(APIView):
    def post(self, request):
        data = request.data['body']
        try:
            User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                first_name=data['firstname'],
                last_name=data['lastname'])

        except IntegrityError:
            return JsonResponse(data={"err": 'Username Already exists'})

        user_info = UserProfile()
        user_info.user = User.objects.get(username=data['username'])
        user_info.save()
        return JsonResponse(data={'err': 0})


class Login(APIView):
    def post(self, request):
        data = request.data['body']

        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse(data={'err': 'Login Error'})

        login(request, user)
        return JsonResponse(data={'user': str(request.user.username)})


def logout_view(request):
    logout(request)
    return JsonResponse(data={"user": request.user.username})


class GetUserInfo(APIView):
    def get(self, request):
        '''Возвращает всю инфу о пользователе. 3 сценария
        1) В параметрах request.GET не послан id, и пользователь не авторизован -> Ошибка
        2) В параметрах request.GET послан id -> инфа о пользователе с id
        3) В параметрах request.GET не послан id, но пользователь авторизован -> инфа об авторизованном пользователе'''

        u_id = request.GET.get('id')
        print(request.user, u_id)
        if (request.user.is_anonymous) and (u_id is None):
            return JsonResponse(data={"err": "You are not logged and id==\'\'"})

        if u_id is not None:
            target_id = u_id
        else:
            target_id = request.user.id

        user_info = UserProfile.get_info_by_user_id(target_id=target_id)
        if user_info is None:
            return JsonResponse(data={"err": "This User Does Not Exists"})

        serializer = UserSerializer(user_info)
        return JsonResponse(data=serializer.data)


class UpdateUserInfo(APIView):
    def put(self, request):
        raise NotImplementedError

        data = request.data.get('body')

        user_info = UserProfile.get_info_by_user_id(data['main_user']['id'])

        serializer = UserSerializer(data=data, instance=user_info)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print("OKE")

        pass
