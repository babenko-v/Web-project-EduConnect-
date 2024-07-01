from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms


from users.models import Teacher_profile, Locations
from teachers.models import  Specializations


class TeacherLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = Teacher_profile
        fields = ('username', 'password')

class TeacherRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    locations = forms.ModelChoiceField(queryset=Locations.objects.all())
    main_specialty = forms.ModelChoiceField(queryset=Specializations.objects.all())

    class Meta:
        model = Teacher_profile
        fields = ('first_name',
                  'last_name',
                  'username',
                  'password1',
                  'password2',
                  'locations',
                  'main_specialty')

class ProfileUpdateForm(UserChangeForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.CharField()
    experience = forms.CharField()
    info_about_teacher = forms.CharField()
    work_experience = forms.CharField()
    other_specialities = forms.CharField()
    education = forms.CharField()

    locations = forms.ModelChoiceField(queryset=Locations.objects.all())

    class Meta:
        model = Teacher_profile
        fields = ('first_name',
                  'last_name',
                  'age',
                  'experience',
                  'info_about_teacher',
                  'work_experience',
                  'other_specialities',
                  'education',
                  'locations'
                  )