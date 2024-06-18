from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db.models import IntegerField

from teachers.models import Specializations

class Locations(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'location'
        ordering = ['name',]

    def __str__(self):
        return self.name

class Contact_info(models.Model):
    phone = IntegerField(verbose_name='phone number')
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
    telegram = models.CharField(max_length=50, unique=True, blank=True, null=True)
    facebook = models.CharField(max_length=100, unique=True, blank=True, null=True)
    instagram = models.CharField(max_length=50, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return self.email


class Mode_teaching(models.Model):
    name_mode = models.CharField(max_length=20, unique=True, verbose_name='mode_teaching')

    class Meta:
        db_table = 'mode_of_teaching'

    def __str__(self):
        return self.name_mode


class Teacher_profile(AbstractUser):
    age = models.PositiveIntegerField()
    experience = models.PositiveIntegerField(default=0)
    info_about_teacher = models.TextField()
    work_experience = models.TextField()
    education = models.TextField()
    other_specialities = models.TextField()
    locations = models.ForeignKey(to=Locations, on_delete=models.CASCADE)
    main_specialty = models.ForeignKey(to=Specializations, on_delete=models.CASCADE)
    contact_info = models.ForeignKey(to=Contact_info, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='profile_image')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'




