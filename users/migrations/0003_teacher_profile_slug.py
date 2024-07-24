# Generated by Django 4.2.7 on 2024-07-24 23:00

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_teacher_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_profile',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=False, null=True, populate_from='get_full_name', unique=True),
        ),
    ]
