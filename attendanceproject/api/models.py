from django.db import models

# Create your models here.
class student_table(models.Model):
    AP_ID = models.IntegerField(null = False, blank=False, unique=True)
    prn = models.CharField(max_length=50, blank=True)
    fname = models.CharField(max_length=254, blank=True)
    lname = models.CharField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=254, blank=True)
    clg_email = models.EmailField(max_length=254, blank=True)
    personal_email = models.EmailField(max_length=254, blank=True)
    password = models.CharField(max_length=254, blank=True)
    status = models.BooleanField(default=False, blank=True)

class teacher_table(models.Model):
    AP_ID = models.IntegerField(null = False, blank=False, unique=True)
    prn = models.CharField(max_length=50, blank=True)
    fname = models.CharField(max_length=254, blank=True)
    lname = models.CharField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=254, blank=True)
    clg_email = models.EmailField(max_length=254, blank=True)
    personal_email = models.EmailField(max_length=254, blank=True)
    password = models.CharField(max_length=254, blank=True)
    status = models.BooleanField(default=False, blank=True)