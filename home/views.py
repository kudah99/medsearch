from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import City, HealthFacility,HealthFacilityCategory,HealthSpecialist,MedicalSpecialty
from django.db.models import Q

def index(request):
    cities = City.objects.all()
    category = HealthFacilityCategory.objects.get(id=1)
    mental_health_facilities  = HealthFacility.objects.filter(category=category)
    medical_specialties = MedicalSpecialty.objects.all()
    context = {'cities': cities, 'mental_health_facilities': mental_health_facilities, 'medical_specialties': medical_specialties}

    return render(request, 'index.html',context=context)



def search_specialists(request):
    if request.method == 'POST':
        medical_specialty = request.POST.get('medical_specialty')
        city = request.POST.get('city')

        # Perform the search based on the form input
        results = HealthSpecialist.objects.filter(
            medical_specialty__name__icontains=medical_specialty,
            city__id=city
        )
        return render(request, f'health_specialists.html', {'results': results})

def health_specialist(request):

    # Get query parameters from the request
    full_name = request.GET.get('full_name', default='')
    city_id = request.GET.get('city', default='')
    medical_specialty_id = request.GET.get('medical_specialty', default='')
    cities = City.objects.all()
    health_facilities  = HealthFacility.objects.all()
    medical_specialties = MedicalSpecialty.objects.all()

    # Build a filter based on the query parameters
    filter_args = Q()
    if full_name:
        filter_args &= Q(full_name__icontains=full_name)
    if city_id:
        filter_args &= Q(city__id=city_id)
    if medical_specialty_id:
        filter_args &= Q(medical_specialty__id=medical_specialty_id)

    # Apply the filter to the queryset
    health_specialists = HealthSpecialist.objects.filter(filter_args)

    context = {'health_specialists': health_specialists,'cities': cities,'health_facilities':health_facilities,'medical_specialties': medical_specialties}
    return render(request, 'health_specialist_list.html', context=context)