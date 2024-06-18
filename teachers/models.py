from django.db import models

class specializations(models.Model):
    name = models.CharField(max_length=150, unique=True,)

    class Meta:
        db_table = 'specialization'
        ordering = ['id',]

