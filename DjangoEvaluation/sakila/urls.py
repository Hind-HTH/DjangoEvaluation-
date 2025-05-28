from django.urls import path
from .views import status, countries, city, city_detail

urlpatterns = [
    path('', status, name = ('banniere') ),
    path('countries/', countries, name='countries'),
    path('cities/', city, name='city'),
    path('cities/<int:city_id>/detail/', city_detail, name='city_detail'),
]