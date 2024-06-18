from django.contrib import admin

from users.models import Mode_teaching, Teacher_profile, Contact_info, Locations

admin.site.register(Mode_teaching)
admin.site.register(Teacher_profile)
admin.site.register(Contact_info)
admin.site.register(Locations)