from django_filters import rest_framework as filters
from .models import Event, UserProfile


class DateFilterInFilter(filters.BaseInFilter, filters.DateFilter):
    pass


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


# class BooleanFilterInFilter(filters.BaseInFilter, filters.BooleanFilter):
#     pass


class EventFilter(filters.FilterSet):
    latitude = filters.RangeFilter()
    longitude = filters.RangeFilter()
    date = DateFilterInFilter(field_name='date', lookup_expr='in')
    type = CharFilterInFilter(field_name='type', lookup_expr='in')

    class Meta:
        model = Event
        fields = ['latitude', 'longitude', 'date', 'type']


# todo
class UserProfileFilter(filters.FilterSet):

    class Meta:
        model = UserProfile
        fields = []

