from django.contrib import admin
from .models import *


class VolunteerAdmin(admin.ModelAdmin):
    search_fields = ['volunteer_id', 'surname', 'fore_names', 'created', 
                     'modified', 'surgery_id__name']
    date_hierarchy = 'dob'

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Volunteer, VolunteerAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    search_fields = ['volunteer_id__surname', 'volunteer_id__fore_names', 'app_date', 'created', 'modified', 'app_status']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Appointment, AppointmentAdmin)


class SurgeryAdmin(admin.ModelAdmin):

    search_fields = ['name', 'post_code', 'created', 'modified']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Surgery, SurgeryAdmin)


class GPAdmin(admin.ModelAdmin):
    search_fields = ['gp_name', 'created', 'modified']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(GP, GPAdmin)
