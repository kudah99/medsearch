from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import City, Contact, HealthFacilityCategory, HealthFacility

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

admin.site.register(City, CityAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(HealthFacilityCategory, HealthFacilityCategoryAdmin)
admin.site.register(HealthFacility, HealthFacilityAdmin)
