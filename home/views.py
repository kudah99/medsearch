from django.shortcuts import render, get_object_or_404,redirect
from .models import City


def index(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'index.html',context=context)
