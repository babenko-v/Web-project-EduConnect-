from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import Http404

from teachers.models import Specializations
from users.models import Locations, Mode_teaching, Teacher_profile

def roster(request, specialization_category=''):
    mode = Mode_teaching.objects.all()
    locality = Locations.objects.all()
    specializations = Specializations.objects.all()

    if specialization_category:
        profiles = Teacher_profile.objects.filter(main_specialty__name_spec=specialization_category)
        if not profiles.exists():
            raise Http404()
    else:
        profiles = Teacher_profile.objects.all()

    # Пагинация
    paginator = Paginator(profiles, 1)  # Количество элементов на странице
    page_number = request.GET.get('page', 1)

    try:
        current_page = paginator.page(page_number)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)

    context = {
        'profiles': current_page,
        'modes': mode,
        'locality': locality,
        'specializations': specializations,
        'specializations_name': specialization_category,
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