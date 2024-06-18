from django.shortcuts import render

from teachers.models import Specializations
from users.models import Locations, Mode_teaching

def roster(request):

    mode = Mode_teaching.objects.all()
    locality = Locations.objects.all()
    specializations = Specializations.objects.all()

    context = {
        'first_name': 'Margaret',
        'last_name': 'Bulishko',
        'phone': '067554212',
        'age': '22',
        'experience': '3',
        'specialization': 'English, Polish, Ukrainian language teacher',
        'modes' : mode,
        'locality' : locality,
        'specializations' : specializations
    }
    return render(request, "teachers/roster_mentors.html", context)

def mentors(request):
    context = {
        'first_name': 'Margaret',
        'last_name': 'Bulishko',
        'phone': '067554212',
        'age': '22',
        'experience': '3',
        'specialization': 'English, Polish, Ukrainian language teacher'
    }
    return render(request, "teachers/card_mentor.html", context)