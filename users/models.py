
from django.contrib.auth.models import AbstractUser
from django.db import models


from django.db.models import IntegerField

from teachers.models import Specializations


class Locations(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'location'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Contact_info(models.Model):
    phone = IntegerField(verbose_name='phone number', blank=True, null=True)
    telegram = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.CharField(max_length=100, unique=True, blank=True, null=True)
    instagram = models.CharField(max_length=50, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return str(self.id)


class Mode_teaching(models.Model):
    name_mode = models.CharField(max_length=20, verbose_name='mode_teaching')

    class Meta:
        db_table = 'mode_of_teaching'

    def __str__(self):
        return self.name_mode

class Teacher_profile(AbstractUser):
    username = models.CharField(unique=True, max_length=50, verbose_name='identifier')
    password = models.CharField(max_length=150)
    age = models.IntegerField(null=True, blank=True)
    experience = models.PositiveIntegerField(default=0, null=True, blank=True)
    info_about_teacher = models.TextField(null=True, blank=True)
    work_experience = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    other_specialities = models.TextField(null=True, blank=True)

    locations = models.ForeignKey(to=Locations, blank=True, null=True, on_delete=models.PROTECT)
    main_specialty = models.ForeignKey(to=Specializations, blank=True, null=True, on_delete=models.PROTECT)
    contact_info = models.OneToOneField(to=Contact_info, blank=True, null=True,  on_delete=models.PROTECT)
    mode_teaching = models.ForeignKey(to=Mode_teaching, blank=True, null=True, on_delete=models.PROTECT)

    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='profile_image')

class Meta:
    db_table = 'info_teacher'
    ordering = ('id',)

def __str__(self):
    return f'{self.last_name} {self.first_name}'
