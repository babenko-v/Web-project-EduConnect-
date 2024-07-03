from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from teachers.models import Specializations
from users.models import Locations, Mode_teaching, Teacher_profile
from users.forms import TeacherLoginForm, TeacherRegisterForm, ProfileUpdateForm


def profile(request):
    profiles = Teacher_profile.objects.filter(id=2)

    context = {
        "profiles": profiles,
    }

    return render(request, "users/profile.html", context)

def change_profile(request):
    modes = Mode_teaching.objects.all()
    locations = Locations.objects.all()

    specializations = Specializations.objects.all()

    if request.method == 'POST':
        form = ProfileUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('main:main'))

    else:
        form = ProfileUpdateForm(instance=request.user)


    context = {
        'modes': modes,
        'locations': locations,
        'form': form,
        'specializations': specializations
    }

    return render(request, 'users/change_profile.html', context)


def login_view(request):
    if request.method == 'POST':
        form = TeacherLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print(f"Username: {username}, Password: {password}")  # Отладочный вывод
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                print("User authenticated and logged in successfully.")  # Отладочный вывод
                return HttpResponseRedirect(reverse('main:main'))
            else:
                print("Authentication failed. User not found or password incorrect.")  # Отладочный вывод
    else:
        form = TeacherLoginForm()

    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)



def registration(request):
    specializations = Specializations.objects.all()
    locations = Locations.objects.all()

    if request.method == 'POST':
        form = TeacherRegisterForm(data=request.POST)

        if form.is_valid():
            form.save()
            users = form.instance
            auth.login(request, users)
            return HttpResponseRedirect(reverse('main:main'))

    else:
        form = TeacherRegisterForm()

    context = {
        'specializations': specializations,
        'locations': locations,
        'form': form
    }

    return render(request, "users/registration.html", context=context)

def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main'))