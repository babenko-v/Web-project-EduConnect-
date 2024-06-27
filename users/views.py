from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from teachers.models import Specializations
from users.models import Locations, Mode_teaching, Teacher_profile
from users.forms import TeacherLoginForm, TeacherRegisterForm


def profile(request):
    modes = Mode_teaching.objects.all()
    profiles = Teacher_profile.objects.filter(id=3)



    list_conact_info = ('phone', 'telegram', 'email', 'instagram')

    context = {
        'modes': modes,
        "profiles": profiles,
        'list_contact': list_conact_info,

    }

    return render(request, "users/profile.html", context)


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
        # pre_form = TeacherRegisterForm(data=request.POST)
        # pre_form.locations = locations.get(name=request.POST['locations']).id
        # pre_form.main_specialty = specializations.get(name_spec=request.POST['main_specialty']).id
        # form = pre_form


        form = TeacherRegisterForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('users:login')

    else:
        form = TeacherRegisterForm()

    context = {
        'specializations': specializations,
        'locations': locations,
        'form': form
    }

    return render(request, "users/registration.html", context=context)