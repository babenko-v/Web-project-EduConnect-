from django.contrib.auth.forms import AuthenticationForm
from django import forms

from users.models import Teacher_profile


class TeacherLoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = Teacher_profile
        fields = ('username', 'password')