from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from teachers.models import Specializations
from users.models import Locations, Mode_teaching, Teacher_profile
from users.forms import TeacherLoginForm


def profile(request):
    modes = Mode_teaching.objects.all()
    profiles = Teacher_profile.objects.filter(id=1)

    list_conact_info = ('phone', 'telegram', 'email', 'instagram')

    context = {
        'modes': modes,
        "profiles": profiles,
        'list_contact': list_conact_info
    }

    return render(request, "users/profile.html", context)


def login(request):
    if request.method == 'POST':
        form = TeacherLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('main:main')
    else:
        form = TeacherLoginForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)



def registration(request):
    specializations = Specializations.objects.all()
    locations = Locations.objects.all()

    context = {
        'specializations': specializations,
        'locations': locations,
    }

    return render(request, "users/registration.html", context=context)