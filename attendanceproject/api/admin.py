from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(student_table)
class student_table(admin.ModelAdmin):
    list_display = ['id', "AP_ID", "fname", "lname", "phone_number", "clg_email", "personal_email", "password", "status"]

@admin.register(teacher_table)
class teacher_table(admin.ModelAdmin):
    list_display = ['id', "AP_ID", "fname", "lname", "phone_number", "clg_email", "personal_email", "password", "status"]