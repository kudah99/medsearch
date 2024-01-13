from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import City, Contact, HealthFacilityCategory, HealthFacility,HealthSpecialist, MedicalSpecialty

class CityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'created_at', 'updated_at')
    search_fields = ('email', 'phone_number')

class HealthFacilityCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)

class HealthFacilityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'description', 'city', 'category', 'contact_info', 'latitude', 'longitude', 'created_at', 'updated_at')
    search_fields = ('name', 'city__name', 'category__name')

class HealthSpecialistResource(resources.ModelResource):
    class Meta:
        model = HealthSpecialist
        
class HealthSpecialistAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('full_name', 'professional_title', 'city', 'medical_specialty', 'contact_info', 'created_at', 'updated_at')
    search_fields = ('full_name', 'city__name', 'medical_specialty__name')

    resource_class = HealthSpecialistResource

class MedicalSpecialtyResource(resources.ModelResource):
    class Meta:
        model = MedicalSpecialty

class MedicalSpecialtyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','image','name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)

    resource_class = MedicalSpecialtyResource

admin.site.register(City, CityAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(HealthFacilityCategory, HealthFacilityCategoryAdmin)
admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(HealthSpecialist, HealthSpecialistAdmin)
admin.site.register(MedicalSpecialty, MedicalSpecialtyAdmin)