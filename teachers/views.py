from django.shortcuts import render

from teachers.models import Specializations
from users.models import Locations, Mode_teaching, Teacher_profile


def roster(request):

    mode = Mode_teaching.objects.all()
    locality = Locations.objects.all()
    specializations = Specializations.objects.all()
    profiles = Teacher_profile.objects.all()

    context = {
        'profiles': profiles,
        'modes' : mode,
        'locality' : locality,
        'specializations' : specializations
    }
    return render(request, "teachers/roster_mentors.html", context)

def mentors(request):
    profiles = Teacher_profile.objects.filter(id=1)

    context = {
        "profiles": profiles,
        'first_name': 'Margaret',
        'last_name': 'Bulishko',
        'phone': '067554212',
        'age': '22',
        'experience': '3',
        'specialization': 'English, Polish, Ukrainian language teacher'
    }
    return render(request, "teachers/card_mentor.html", context)