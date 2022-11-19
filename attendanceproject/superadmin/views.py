from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django import forms
from attendanceproject.settings import MEDIA_URL
from .models import *
from .data_base_admin import *
from .import urls
import pymongo
import csv
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import constants as messages
from django.utils.decorators import method_decorator
import superadmin.authenticate_user as au
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
Session.objects.all().delete()


# Create your views here.
# User Name

client = pymongo.MongoClient("mongodb+srv://harsh:harsh@attendanceproject.rrlaxic.mongodb.net/?retryWrites=true&w=majority") 
db = client['AttendanceProject']
collection = db['superadmin_createaccounts']


# @au.entry_check
def AdminHome(request):
        value = request.session.get('user')
        permission = au.check_if_allowed(value)
        if permission == True:
                return render(request, 'superadmin/index.html')
        else:
                return redirect('Login')
        

def check(request):
        return HttpResponse("HELLO PPL")

@csrf_exempt
def Login(request):
        try:
                if request.method=="POST":
                        admin_name = request.POST.get("adminName")
                        admin_password = request.POST.get("adminPassword")
                        user_auth = au.auth_user(admin_name, admin_password)
                        if user_auth == True:
                                request.session['user'] = admin_name
                                return redirect('AdminHome')
                        else:
                                return redirect('SignUp')
                return render(request, 'superadmin/login.html')
        except Exception as e:
                print("----------------------------------------------------------------------")
                print(e)
                return render(request, 'superadmin/login.html')


        

def MakeAccounts(CsvFile):
        db = client['AttendanceProject']
        collection = db['superadmin_createaccounts']
        data = []
        base = 'attendanceproject/media/'
        FileWithLocation = base+str(CsvFile)
        # FileWithLocation = '../attendanceproject/media/'+str(CsvFile)
        # C:\Users\Harsh\Desktop\\hovertap\attendanceproject\media\FYBTECHDATA_vU0v8V6.csv
        print(FileWithLocation)
        with open(FileWithLocation) as f:
                reader = csv.reader(f)
                for i in reader:
                        dict1 = {'studentPrn':i[0],'studentName':i[1],'studentEmail':i[2],'studentNumber':i[3]}
                        data.append(dict1)
        collection.insert_many(data)

# @au.entry_check
def SaveData(request):
        value = request.session.get('user')
        permission = au.check_if_allowed(value)
        if permission == True:
                redirect('UploadFiles')
                if request.method=="POST":
                        coures = request.POST.get("coures")
                        branch = request.POST.get("branch")
                        year = request.POST.get("year")
                        file_csv = request.FILES["file_csv"]
                        data = FileUpload.objects.create(coures=coures,branch=branch,year=year,file=file_csv)
                        data.save()
                        MakeAccounts(file_csv) 
                return render(request, 'superadmin/uploadfile.html')
        else:
             return redirect('Login')   

# @au.entry_check
def ShowAccounts(request):
        value = request.session.get('user')
        permission = au.check_if_allowed(value)
        if permission == True:
                StudentDetails = CreateAccounts.objects.all()
                context = {'details':StudentDetails}
        # for item in StudentDetails:
        #         print(item.studentPrn,item.studentName, item.studentEmail, item.studentNumber)
                return render(request, 'superadmin/UpdateStudent.html', context)
        else:
                return redirect('Login')





def SignUp(request):
         return render(request, 'superadmin/signup.html')


def ForgotPassword(request):
        return render(request, 'superadmin/forgot.html')

def AddCourse(request):
        if request.method=="POST":
               course_id = request.POST.get("course_id")
               course_name = request.POST.get("course_name")
               data = Course.objects.create(course_id=course_id, course_name=course_name)
               data.save()
               return redirect('AddCourse')
        #        course_details = Course.objects.all()
        #        context = {'details':course_details}
               
        else:
               return render(request, 'superadmin/addcourse.html')

def course(request):
        course_details = Course.objects.all()
        context = {'details':course_details}
        return render(request, 'superadmin/course.html',context)

def ShowAllCourse(request):
        if request.method=="POST":
                course_details = Course.objects.all()
                course_count = len(course_details)
                empty = []
                for i in course_details:
                        cid = i.course_id
                        cn = i.course_name
                        var = {
                                "RecordID": cid,
                                "course_id":cid,
                                "course_name":cn,
                                # "Actions": "null"
                        }
                        empty.append(var)

                        dict1 = {
                                "meta": {
                                        "page": 1,
                                        "pages": 1,
                                        "perpage": -1,
                                        "total": course_count,
                                        "sort": "asc",
                                        "field": "RecordID"
                                        },
                                "data": empty
                                }
        letscheck = json.dumps(dict1)
        # return letscheck
        return HttpResponse(letscheck)


def year(request):
        course_details = Course.objects.all()
        year_details = Year.objects.all()
        context = {'details':course_details,'details2':year_details} 
        return render(request, 'superadmin/year.html',context)

def AddYear(request):
        if request.method=="POST":
               year_id = request.POST.get("year_id")
               year_number = request.POST.get("year_number")
               data = Year.objects.create(year_id=year_id,year_number=year_number)
               data.save()
               return redirect('AddYear')
        #        course_details = Course.objects.all()
        #        context = {'details':course_details}
               
        else:
               return render(request, 'superadmin/addyear.html')
        


def division(request):
        course_details = Course.objects.all()
        year_details = Year.objects.all()
        division_name = Division.objects.all()
        context = {'details':course_details,'details2':year_details,'details3':division_name} 
        return render(request, 'superadmin/division.html')

def AddDivision(request):
        if request.method=="POST":
               division_name = request.POST.get("division_name")
               data = Division.objects.create(division_name=division_name)
               data.save()
               return redirect('AddYear')
        #        course_details = Course.objects.all()
        #        context = {'details':course_details}
               
        else:
               return render(request, 'superadmin/adddivision.html')
        




def subject(request):
        course_details = Course.objects.all()
        context = {'details':course_details} 
        return render(request, 'superadmin/subject.html',context)

def AddSubject(request):
        return render(request, 'superadmin/addsubject.html')