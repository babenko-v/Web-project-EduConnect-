from django.db import models

class Specializations(models.Model):
    name_spec = models.CharField(max_length=150, unique=True)

    class Meta:
        db_table = 'specialization'
        ordering = ['id',]

    def __str__(self):
        return self.name_spec

