from django.db import models

# Create your models here.
class student_table(models.Model):
    AP_ID = models.IntegerField(null = False, blank=False, unique=True)
    name = models.EmailField(max_length=50, null = False)
    password = models.CharField(max_length=254)
    status = models.BooleanField(default=False)
