import re

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.core.exceptions import ValidationError

from users.models import Teacher_profile, Locations, Mode_teaching
from teachers.models import  Specializations
from users.utils import numeric_validator, fullname_validator


class TeacherLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = Teacher_profile
        fields = ('username', 'password')

class TeacherRegisterForm(UserCreationForm):
    first_name = forms.CharField(validators=[fullname_validator])
    last_name = forms.CharField(validators=[fullname_validator])
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

    first_name = forms.CharField(validators=[fullname_validator])
    last_name = forms.CharField(validators=[fullname_validator])
    username = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    age = forms.CharField(required=False, validators=[numeric_validator])
    experience = forms.CharField(required=False, validators=[numeric_validator])
    info_about_teacher = forms.CharField(required=False)
    work_experience = forms.CharField(required=False)
    other_specialities = forms.CharField(required=False)
    education = forms.CharField(required=False)

    locations = forms.ModelChoiceField(queryset=Locations.objects.all())
    main_specialty = forms.ModelChoiceField(queryset=Specializations.objects.all(), required=False)
    mode_teaching = forms.ModelChoiceField(queryset=Mode_teaching.objects.all(), required=False)

    def clean_phone(self):
        data = self.cleaned_data['phone']

        if not data.isdigit():
            raise forms.ValidationError("The phone number must contain only digits")

        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError("The phone number must be 10 digits long")

        return data
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', email):
            raise ValidationError("The email must include @gmail.com and be in English.")
        return email



    class Meta:
        model = Teacher_profile
        fields = ('first_name',
                  'last_name',
                  'username',
                  'age',
                  'experience',
                  'info_about_teacher',
                  'work_experience',
                  'other_specialities',
                  'education',
                  'locations',
                  'main_specialty',
                  'mode_teaching',
                  'phone',
                  'email'
                  )


