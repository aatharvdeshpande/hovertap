from django.db import models

# Create your models here.
class Students(models.Model):
    studentEmail = models.EmailField(max_length=200)
    studentPassword = models.CharField(max_length=100)

