from django.shortcuts import render, get_object_or_404,redirect
from .models import City, HealthFacility,HealthFacilityCategory,HealthSpecialist


def index(request):
    cities = City.objects.all()


    category = HealthFacilityCategory.objects.get(id=1)
    mental_health_facilities  = HealthFacility.objects.filter(category=category)
    context = {'cities': cities, 'mental_health_facilities': mental_health_facilities}
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

