from django.db import models

# Create your models here.

class FileUpload(models.Model):
    coures = models.CharField(max_length=50, null = True)
    branch = models.CharField(max_length=50, null = True)
    year = models.IntegerField(default = 1, null = True)
    file = models.FileField(null = True)
    

class CreateAccounts(models.Model):
    studentPrn = models.IntegerField(null = False, blank=False, unique=True)
    studentName = models.CharField(max_length=50, null = False)
    studentEmail = models.EmailField(max_length=254)
    studentNumber = models.IntegerField(null = True, blank=False, unique=True)

class AdminAccount(models.Model):
    AP_ID = models.IntegerField(null = False, blank=False, unique=True)
    adminName = models.CharField(max_length=50, null = False)
    adminEmail = models.EmailField(max_length=254)
    adminPassword = models.CharField(max_length=50, null = False)
    loginStatus = models.BooleanField(default = False) 

class Course(models.Model):
    course_id = models.IntegerField(null = False, blank = False, unique = True, primary_key=True)
    course_name = models.CharField(max_length=50, null = False)

class Year(models.Model):
    year_id = models.IntegerField(null = False, blank = False, unique = True, primary_key=True)
    year_number = models.IntegerField(null = False, blank = False, unique = True)
    
class Subject(models.Model):
    # year_id = models.IntegerField(null = False, blank = False, unique = True, primary_key=True)
    subject_name = models.CharField(max_length=50, null = False)

class Division(models.Model):
    # year_id = models.IntegerField(null = False, blank = False, unique = True, primary_key=True)
    division_name = models.CharField(max_length=50, null = False)