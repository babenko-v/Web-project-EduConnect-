from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from teachers.models import Specializations
from users.models import Locations, Mode_teaching, Teacher_profile
from users.forms import TeacherRegisterForm, ProfileUpdateForm


class TeacherProfileView(LoginRequiredMixin, DetailView):
    template_name = "users/profile.html"
    context_object_name = 'profiles'

    def get_object(self, **kwargs):
        profiles = Teacher_profile.objects.filter(id=self.request.user.id)
        return profiles


class TeacherProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "users/change_profile.html"
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        messages.success(self.request, "You have successfully change info into your account.")
        return super().form_valid(form)

    def get_object(self, **kwargs):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        context['specializations'] = Specializations.objects.all()
        context['modes'] = Mode_teaching.objects.all()
        return context



# @login_required
# def change_profile(request):
#     modes = Mode_teaching.objects.all()
#     locations = Locations.objects.all()
#
#     specializations = Specializations.objects.all()
#
#     if request.method == 'POST':
#         form = ProfileUpdateForm(data=request.POST, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             messages.success(request, "You have successfully change info into your account.")
#
#             return HttpResponseRedirect(reverse('main:main'))
#
#     else:
#         form = ProfileUpdateForm(instance=request.user)
#
#
#     context = {
#         'modes': modes,
#         'locations': locations,
#         'form': form,
#         'specializations': specializations
#     }
#
#     return render(request, 'users/change_profile.html', context)

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm


    def get_success_url(self):
        messages.success(self.request, "You are now logged in.")
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('users:logout'):
            return redirect_page
        return reverse_lazy('main:main')




class UserRegestrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = TeacherRegisterForm
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        users = form.save()
        auth.login(self.request, users)
        messages.success(self.request, "You have successfully registered and logged into your account.")
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Locations.objects.all()
        context['specializations'] = Specializations.objects.all()
        return context


@login_required
def logout_view(request):
    messages.success(request, "You have successfully log out your account.")
    auth.logout(request)

    return HttpResponseRedirect(reverse('main:main'))

# def login_view(request):
#     if request.method == 'POST':
#         form = TeacherLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             print(f"Username: {username}, Password: {password}")  # Отладочный вывод
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 print("User authenticated and logged in successfully.")  # Отладочный вывод
#
#                 redirect_page = request.POST.get('next', None)
#
#                 messages.success(request, "You are now logged in.")
#
#                 if redirect_page and redirect_page != reverse('users:logout'):
#                     return HttpResponseRedirect(request.POST.get('next'))
#                 return HttpResponseRedirect(reverse('main:main'))
#             else:
#                 print("Authentication failed. User not found or password incorrect.")  # Отладочный вывод
#                 messages.success(request, "You aren't now logged in.")
#     else:
#         form = TeacherLoginForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'users/login.html', context)

# def registration(request):
#     specializations = Specializations.objects.all()
#     locations = Locations.objects.all()
#
#     if request.method == 'POST':
#         form = TeacherRegisterForm(data=request.POST)
#
#         if form.is_valid():
#             form.save()
#             users = form.instance
#             auth.login(request, users)
#             messages.success(request, "You have successfully registered and logged into your account.")
#             return HttpResponseRedirect(reverse('main:main'))
#
#     else:
#         form = TeacherRegisterForm()
#
#     context = {
#         'specializations': specializations,
#         'locations': locations,
#         'form': form
#     }
#
#     return render(request, "users/registration.html", context=context)

# @login_required
# def profile(request):
#     profiles = Teacher_profile.objects.filter(id=request.user.id)
#
#     context = {
#         "profiles": profiles,
#     }
#
#     return render(request, "users/profile.html", context)