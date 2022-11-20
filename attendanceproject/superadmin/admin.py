from django.contrib import admin
from .models import * 

# Register your models here.
# class MakePanels(admin.ModelAdmin):
#     list_display = ['id', 'year', 'course']

@admin.register(FileUpload)
class FileUpload(admin.ModelAdmin):
    list_display = ['coures', 'branch', 'year', 'file']

@admin.register(CreateAccounts)
class CreateAccounts(admin.ModelAdmin):
    list_display = ['studentPrn','studentName','studentEmail','studentNumber']

@admin.register(AdminAccount)
class AdminAccount(admin.ModelAdmin):
    list_display = ['AP_ID', 'adminName','adminEmail','adminPassword']

@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ['course_name','course_id']

@admin.register(Year)
class Year(admin.ModelAdmin):
    list_display = ['year_id','year_number']

@admin.register(Subject)
class Subject(admin.ModelAdmin):
    list_display = ['subject_id','subject_name']

@admin.register(Division)
class Division(admin.ModelAdmin):
    list_display = ['division_id','division_name']

@admin.register(ClassRoom)
class ClassRoom(admin.ModelAdmin):
    list_display = ['ClassRoom_id','course_name', 'course_year', 'course_division', 'course_subject','file_csv_student','file_csv_teacher']
