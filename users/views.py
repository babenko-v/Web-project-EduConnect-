from django.shortcuts import render

from teachers.models import Specializations
from users.models import Locations, Mode_teaching, Teacher_profile


def profile(request):
    modes = Mode_teaching.objects.all()
    profiles = Teacher_profile.objects.filter(id=1)

    list_conact_info = ('phone', 'telegram', 'facebook', 'instagram')

    context = {
        'modes': modes,
        "profiles": profiles,
        'list_contact': list_conact_info
    }

    return render(request, "users/profile.html", context)

def login(request):
    return render(request, "users/login.html")

def registration(request):
    specializations = Specializations.objects.all()
    locations = Locations.objects.all()

    context = {
        'specializations': specializations,
        'locations': locations,
    }

    return render(request, "users/registration.html", context)