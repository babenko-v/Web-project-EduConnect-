from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from teachers.models import Specializations
from users.models import Locations, Mode_teaching, Teacher_profile
from teachers.utils import search_query

from django.shortcuts import render


def roster(request):

    modes = Mode_teaching.objects.all()
    locality = Locations.objects.all()
    specializations = Specializations.objects.all()

    query = request.GET.get('q')

    profiles = Teacher_profile.objects.all()
    profiles = profiles.exclude(is_staff=True)

    type_std = request.GET.get('type_std')
    speciality = request.GET.get('speciality')
    location = request.GET.get('location')
    sort = request.GET.get('sort')

    if query:
        profiles = search_query(query)
    else:
        ...

    if speciality:
        profiles = profiles.filter(main_specialty__name_spec=speciality)

    if type_std:
        profiles = profiles.filter(mode_teaching__name_mode=type_std)

    if location:
        profiles = profiles.filter(locations__name=location)

    if sort:
        profiles = profiles.order_by(sort)

    # Пагинация
    paginator = Paginator(profiles, 3)  # Количество элементов на странице
    page_number = request.GET.get('page', 1)


    try:
        current_page = paginator.page(int(page_number))
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)

    context = {
        'profiles_amount': profiles.count(),  # Количество профилей, удовлетворяющих фильтрам
        'profiles': current_page,
        'modes': modes,
        'locality': locality,
        'specializations': specializations,

    }

    return render(request, "teachers/roster_mentors.html", context)

def mentors(request, mentors_id):
    profiles = Teacher_profile.objects.filter(id=mentors_id)

    context = {
        "profiles": profiles,
    }
    return render(request, "teachers/card_mentor.html", context=context)