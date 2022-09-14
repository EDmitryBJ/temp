from atexit import register
from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'is_online',
        'about',
        'contacts',
        'subscribers_num',
        'user',
        'filter_settings',
        'image'
    )
    list_display_links = ['user', 'filter_settings']
    filter_horizontal = ('subscriptions', 'black_list')


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'name',
        'image',
        'about',
        'latitude',
        'longitude',
        'date',
        'contacts',
        'timetable',
        'is_private',
        'is_deleted',
        'type'
    )
    list_display_links = ('author', 'contacts')
    filter_horizontal = ['invited_users']


# Register your models here.
# admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(Event, EventAdmin)
admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Contacts)
admin.site.register(FilterSettings)
admin.site.register(EventPlan)
admin.site.register(ShareableEventPlan)
admin.site.register(EventPositionInPlan)
admin.site.register(Chat)
admin.site.register(ChatMessage)
