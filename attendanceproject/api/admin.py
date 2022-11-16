from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(student_table)
class student_table(admin.ModelAdmin):
    list_display = ['id', 'AP_ID', 'name', 'password', 'status']