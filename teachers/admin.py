from django.contrib import admin

from teachers.models import Specializations

# admin.site.register(Specializations)

@admin.register(Specializations)
class SpecializationsAdmin(admin.ModelAdmin):
    list_display = ('name_spec',)
