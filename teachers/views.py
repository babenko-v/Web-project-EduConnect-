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

def mentors(request, mentors_id):
    profiles = Teacher_profile.objects.filter(id=mentors_id)
    list_conact_info = ('phone', 'telegram', 'facebook', 'instagram')


    context = {
        "profiles": profiles,
        'list_contact': list_conact_info
    }
    return render(request, "teachers/card_mentor.html", context=context)