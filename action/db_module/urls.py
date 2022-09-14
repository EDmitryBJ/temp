import djoser
from django.urls import path, include

# from .models import Contacts
from .views import EventAPIList, EventAPIRetrieve, EventAPIUpdate, EventAPIDestroy, EventAPICreate, \
    UserAPIRetrieve, UserProfileAPICreate
from .user_views import *

# todo change path names change PascalCase to "-"
# todo ctrl + alt + l everywhere
urlpatterns = [
    # path('user/login/', UserAPILogout.as_view()),
    # path('user/logout/', UserAPILogout.as_view()),
    # path('user/register/', user_register),
    path('user_profile/create/', UserProfileAPICreate.as_view()),
    path('user_profile/retrieve/<int:pk>/', UserAPIRetrieve.as_view()),
    # todo
    # path('user_profile/update/', UserAPIUpdate.as_view()),
    # path('user/destroy/', UserAPIDestroy.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

    path('events/retrieve/', EventAPIList.as_view()),
    path('event/retrieve/<int:pk>/', EventAPIRetrieve.as_view()),
    path('event/create/', EventAPICreate.as_view()),
    path('event/update/', EventAPIUpdate.as_view()),
    path('event/destroy/', EventAPIDestroy.as_view())
]
