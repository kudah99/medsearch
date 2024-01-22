from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/',views.search_specialists, name='search_specialists'),
     path("medical_specialist/", views.health_specialist, name="medical-specialist"),
     path("health_facility/", views.health_facility, name="health_facility"),
]