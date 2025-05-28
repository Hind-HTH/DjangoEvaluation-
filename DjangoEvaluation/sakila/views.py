from django.shortcuts import render, redirect
from datetime import datetime
from .models import Country, City
from django.db.models import Q
from django.contrib import messages


# def countries(request):
#     return render(request, 'countries.html')

# def villes(request):
#     return render(request, 'villes.html')
def status(request):

    h = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'banniere.html', {'hours': h})



def countries(request):
    countries_list = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries_list})

def city(request):
    cities_list = City.objects.all()
    return render(request, 'city.html', {'cities': cities_list})
