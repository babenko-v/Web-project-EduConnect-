from contextlib import nullcontext

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from pkg_resources import null_ns_handler

from teachers.models import Specializations, Complaints
from users.models import Locations, Mode_teaching, Teacher_profile
from django.core.cache import cache
from teachers.utils import search_query
from teachers.forms import ComplaintForm

from django.shortcuts import render


class RosterView(ListView):
    model = Teacher_profile
    template_name = 'teachers/roster_mentors.html'
    context_object_name = 'profiles'
    paginate_by = 3
    allow_empty = True

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_staff=True)


        query = self.request.GET.get('q')
        type_std = self.request.GET.get('type_std')
        speciality = self.request.GET.get('speciality')
        location = self.request.GET.get('location')
        sort = self.request.GET.get('sort')
        print("v func", queryset)
        print(sort)
        print(Teacher_profile.objects.exclude(is_staff=True).order_by('age'))

        if query:
            queryset = search_query(query)
        if speciality:
            queryset = queryset.filter(main_specialty__name_spec=speciality)
        if type_std:
            queryset = queryset.filter(mode_teaching__name_mode=type_std)
        if location:
            queryset = queryset.filter(locations__name=location)
        if sort:
            queryset = queryset.order_by(sort)
        print("posle", queryset)

        return queryset



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles_amount'] = self.get_queryset().count()
        context['modes'] = Mode_teaching.objects.all()
        context['specializations'] = Specializations.objects.all()

        locations = cache.get('locations')
        if not locations:
            locations = Locations.objects.all()
            cache.set('locations', locations, 180)

        context['locality'] = locations

        return context

class MentorView(DetailView):

    template_name = 'teachers/card_mentor.html'
    pk_url_kwarg = 'mentors_id'
    context_object_name = 'profiles'

    def get_object(self, **kwargs):
        profiles = Teacher_profile.objects.filter(id=self.kwargs.get(self.pk_url_kwarg))
        return profiles

class ComplaintView(CreateView):
    template_name = 'teachers/complaint_to_teacher.html'

    form_class = ComplaintForm
    success_url = reverse_lazy('main:main')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "You have successfully registered and logged into your account.")
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['complaints'] = Complaints.objects.all()
        return context

# def roster(request):
#
#     modes = Mode_teaching.objects.all()
#     locality = Locations.objects.all()
#     specializations = Specializations.objects.all()
#
#     query = request.GET.get('q')
#
#     profiles = Teacher_profile.objects.all()
#     profiles = profiles.exclude(is_staff=True)
#
#     type_std = request.GET.get('type_std')
#     speciality = request.GET.get('speciality')
#     location = request.GET.get('location')
#     sort = request.GET.get('sort')
#
#     if query:
#         profiles = search_query(query)
#     else:
#         ...
#
#     if speciality:
#         profiles = profiles.filter(main_specialty__name_spec=speciality)
#
#     if type_std:
#         profiles = profiles.filter(mode_teaching__name_mode=type_std)
#
#     if location:
#         profiles = profiles.filter(locations__name=location)
#
#     if sort:
#         profiles = profiles.order_by(sort)
#
#     # Пагинация
#     paginator = Paginator(profiles, 3)  # Количество элементов на странице
#     page_number = request.GET.get('page', 1)
#
#
#     try:
#         current_page = paginator.page(int(page_number))
#     except PageNotAnInteger:
#         current_page = paginator.page(1)
#     except EmptyPage:
#         current_page = paginator.page(paginator.num_pages)
#
#     context = {
#         'profiles_amount': profiles.count(),  # Количество профилей, удовлетворяющих фильтрам
#         'profiles': current_page,
#         'modes': modes,
#         'locality': locality,
#         'specializations': specializations,
#
#     }
#
#     return render(request, "teachers/roster_mentors.html", context)

# def mentors(request, mentors_id):
#     profiles = Teacher_profile.objects.filter(id=mentors_id)
#
#     context = {
#         "profiles": profiles,
#     }
#     return render(request, "teachers/card_mentor.html", context=context)
