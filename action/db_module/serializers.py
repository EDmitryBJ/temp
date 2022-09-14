from dataclasses import field
from pkgutil import read_code
from traceback import print_tb

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault, DateField
from rest_framework.relations import PrimaryKeyRelatedField
# from mmap import MAP_DENYWRITE
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, IntegerField, CharField, \
    ReadOnlyField
from .models import UserProfile, Contacts, Event, EventPlan, ShareableEventPlan, Chat, ChatMessage, FilterSettings
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    '''Сериализатор User'''

    class Meta:
        model = User
        fields = '__all__'


class ContactsSerializer(ModelSerializer):
    '''Сериализатор Contacts'''

    class Meta:
        model = Contacts
        fields = '__all__'


class FilterSettingsSerializer(ModelSerializer):
    class Meta:
        model = FilterSettings
        fields = '__all__'


class UserProfileSerializer(ModelSerializer):
    contacts = ContactsSerializer()
    filter_settings = FilterSettingsSerializer()
    user = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        contacts = Contacts.objects.create(
            vk=validated_data['contacts']['vk'],
            telegram=validated_data['contacts']['telegram'],
            instagram=validated_data['contacts']['instagram'],
            web_site=validated_data['contacts']['web_site'],
            email=validated_data['contacts']['email']
        )
        filter_settings = FilterSettings.objects.create()
        user_profile = UserProfile.objects.create(
            user=self.context['request'].user,
            is_online=True,  # todo add check online
            about=validated_data['about'],
            contacts=contacts,
            filter_settings=filter_settings,
        )
        return user_profile

    def to_representation(self, instance):
        representation = super(UserProfileSerializer, self).to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        representation['contacts'] = ContactsSerializer(instance.contacts).data
        representation['filter_settings'] = FilterSettingsSerializer(instance.filter_settings).data
        return representation

    # todo add update


class EventSerializer(ModelSerializer):
    contacts = ContactsSerializer()
    # invited_users = UserSerializer(many=True, read_only=True, required=False)
    # author = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'

        def create(self, validated_data):
            contacts = Contacts.objects.create(
                vk=validated_data['contacts']['vk'],
                telegram=validated_data['contacts']['telegram'],
                instagram=validated_data['contacts']['instagram'],
                web_site=validated_data['contacts']['web_site'],
                email=validated_data['contacts']['email']
            )
            event = Event.objects.create(
                # author=self.context['request'].user,
                contacts=contacts,
                name=validated_data['name'],
                about=validated_data['about'],
                # latitude=validated_data['latitude'],
                # longitude=validated_data['longitude'],
                # date=validated_data['date'],
                # timetable=validated_data['timetable'],
                # is_private=validated_data['is_private'],
                # is_deleted=validated_data['is_deleted'],
                # type=validated_data['type']
            )
            return event

        def to_representation(self, instance):
            representation = super(EventSerializer, self).to_representation(instance)
            # representation['author'] = ContactsSerializer(instance.author).data
            representation['contacts'] = ContactsSerializer(instance.contacts).data
            return representation
