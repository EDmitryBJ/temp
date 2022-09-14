from http.client import HTTPResponse
from sqlite3 import IntegrityError
from traceback import print_tb
from urllib.parse import uses_relative
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import UpdateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, logout, authenticate

from .models import UserProfile, Contacts, Event
from .serializers import EventSerializer, UserProfileSerializer
from .service import EventFilter, UserProfileFilter


# # todo check and delete
# class UserAPILogout(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request):
#         logout(request)
#         return Response(status=status.HTTP_200_OK)
#
#
# # todo check and delete
# class UserAPIRegister(APIView):
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         user_serializer = UserProfileSerializer(data=request.data)
#         user_serializer.is_valid(raise_exception=True)
#         user_serializer.save()
#         return Response(status=status.HTTP_200_OK)
#
#
# # todo delete
# class UserAPILogin(APIView):
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         if not request.data.get('username'):
#             return JsonResponse(data={'error': 'EMPTY_USERNAME'}, status=status.HTTP_400_BAD_REQUEST)
#         if not request.data.get('password'):
#             return JsonResponse(data={'error': 'EMPTY_PASSWORD'}, status=status.HTTP_400_BAD_REQUEST)
#         user = authenticate(username=request.data.get(
#             'username'), password=request.data.get('password'))
#         if user:
#             login(request, user)
#             return Response(status=status.HTTP_200_OK)
#         return JsonResponse(data={'error': 'WRONG_DATA'}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileAPICreate(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)


class UserAPIRetrieve(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)


# #todo
# class UserAPIUpdate(UpdateAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileRetrieveSerializer
#     permission_classes = (IsAuthenticated,)

# #todo
# class UserAPIDestroy(DestroyAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileRetrieveSerializer
#     permission_classes = (IsAuthenticated,)

class EventAPIList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventFilter
    permission_classes = (IsAuthenticated,)


class EventAPIRetrieve(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)


class EventAPIUpdate(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)


class EventAPIDestroy(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)


class EventAPICreate(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)
