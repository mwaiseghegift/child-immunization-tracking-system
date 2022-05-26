from django.contrib import admin
from .models import *

# Register your models here.


class ChildAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'parent', 'doctor', 'created_at']
    list_filter = ['created_at']
    search_fields = ['first_name']

admin.site.register(Child, ChildAdmin)

class ChildImmunizationAdmin(admin.ModelAdmin):
    list_display = ['child', 'vaccine', 'doctor', 'date_given', 'is_vaccinated']
    list_filter = ['date_given', 'is_vaccinated']
    search_fields = ['child']

admin.site.register(ChildImmunization, ChildImmunizationAdmin)

class VaccinesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'time_given', 'order']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Vaccines, VaccinesAdmin)