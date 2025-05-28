from django.urls import path
from .views import status, countries, city

urlpatterns = [
    path('', status, name = ('banniere') ),
    path('countries/', countries, name='countries'),
    path('cities/', city, name='city'),

]