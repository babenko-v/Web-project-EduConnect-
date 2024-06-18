from django.db import models

from django.db.models import IntegerField
# from django.contrib.auth.models import AbstractUser

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


class Teacher_profile(models.Model):
    age = models.IntegerField(null=True, blank=True)
    experience = models.PositiveIntegerField(default=0, null=True, blank=True)
    info_about_teacher = models.TextField(null=True, blank=True)
    work_experience = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    other_specialities = models.TextField(null=True, blank=True)
    locations = models.ForeignKey(to=Locations, on_delete=models.PROTECT)
    main_specialty = models.ForeignKey(to=Specializations, on_delete=models.PROTECT)
    contact_info = models.ForeignKey(to=Contact_info, on_delete=models.PROTECT)

    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='profile_image')

    def __str__(self):
        return f'{self.main_specialty}'




