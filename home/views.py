from django.shortcuts import render, get_object_or_404,redirect
from .models import City, HealthFacility,HealthFacilityCategory


def index(request):
    cities = City.objects.all()


    category = HealthFacilityCategory.objects.get(id=1)
    mental_health_facilities  = HealthFacility.objects.filter(category=category)
    context = {'cities': cities, 'mental_health_facilities': mental_health_facilities}
    return render(request, 'index.html',context=context)
