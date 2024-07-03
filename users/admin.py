from django.contrib import admin

from users.models import Mode_teaching, Teacher_profile, Locations

admin.site.register(Mode_teaching)
admin.site.register(Teacher_profile)
admin.site.register(Locations)