from django.shortcuts import render

from teachers.models import Specializations
from users.models import Locations, Mode_teaching


def profile(request):
    modes = Mode_teaching.objects.all()

    context = {
        'modes': modes,
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