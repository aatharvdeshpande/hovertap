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
                return render(request, 'superadmin/login.html')


        

def MakeAccounts(CsvFile):
        db = client['AttendanceProject']
        collection = db['superadmin_createaccounts']
        data = []
        base = 'media/'
        FileWithLocation = base+str(CsvFile)
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


# @au.entry_check
def Home(request):
        return render(request, 'home/home.html')                





def SignUp(request):
         return render(request, 'superadmin/signup.html')


def ForgotPassword(request):
        return render(request, 'superadmin/forgot.html')

def AddCourse(request):
        if request.method=="POST":
                course_method = request.POST.get("method")
                if course_method == "insert":
                        course_name = request.POST.get("course_name")
                        count = len(Course.objects.all()) + 1
                        data = Course.objects.create(course_id=count,course_name=course_name)
                        data.save()
                        return redirect('ViewCourse')
                elif course_method == "update":
                        course_name = request.POST.get("course_name")
                        course_id = request.POST.get("course_id")
                        record = Course.objects.get(course_id = course_id)
                        record.course_name = course_name
                        record.save()
                        return redirect('ViewCourse')
        #        course_details = Course.objects.all()
        #        context = {'details':course_details}

def ViewCourse(request):
        course_details = Course.objects.all()
        context = {'details':course_details, 'method':"insert"}
        return render(request, 'superadmin/course.html',context)

def EditCourse(request,id):
        course_details = Course.objects.get(course_id = id)
        context = {'details':course_details, 'method':"update"}
        return render(request, 'superadmin/EditCourse.html', context)

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
        


def Division(request):
        # course_details = Course.objects.all()
        # year_details = Year.objects.all()
        # division_name = Division.objects.all()
        # context = {'details':course_details,'details2':year_details,'details3':division_name} 
        return render(request, 'superadmin/division.html')

def AddDivision(request):
        if request.method=="POST":
               division_name = request.POST.get("division_name")
               data = Division.objects.create(division_name=division_name)
               data.save()
               return redirect('AddYear')              
        else:
               return render(request, 'superadmin/adddivision.html')
        




def Subject(request):
        classroom_details = ClassRoom.objects.all()
        course_details = Course.objects.all()
        context = {'details':course_details, 'method':"insert",'classroom':classroom_details} 
        return render(request, 'superadmin/subject.html',context)

def AddSubject(request):
        if request.method=="POST":
                course_method = request.POST.get("method")
                if course_method == "insert":
                        count = len(ClassRoom.objects.all()) + 1
                        course_name = request.POST.get("course")
                        course_year = request.POST.get("year")
                        course_division = request.POST.get("division")
                        subjects = request.POST.get("subject")
                        course_subject = [x.strip() for x in subjects.split(',')][:-1]
                        file_csv_student = request.FILES["file_csv_student"]
                        file_csv_teacher = request.FILES["file_csv_teacher"]
                        data = ClassRoom.objects.create(ClassRoom_id=count,course_name=course_name,course_year=course_year,course_division=course_division,course_subject=subjects,file_csv_student=file_csv_student, file_csv_teacher= file_csv_teacher)
                        data.save()
                        student_list = au.student_details(file_csv_student)
                        teacher_list = au.teacher_details(file_csv_teacher)
                        where = {'ClassRoom_id':count}
                        store1 = au.update_s_t(where,student_list,teacher_list)
                        sql = {
                                'ClassRoom_id':count,
                                'course_name':course_name,
                                'course_year':course_year,
                                'course_division':course_division,
                                'course_subject':course_subject
                        }

                        return redirect('Subject')
                elif course_method == "update":
                        classroom_id = request.POST.get("classroom_id")
                        course_name = request.POST.get("course")
                        course_year = request.POST.get("year")
                        course_division = request.POST.get("division")
                        subjects = request.POST.get("subject")
                        course_subject = [x.strip() for x in subjects.split(',')][:-1]      
                        sql = {
                                'course_name':course_name,
                                'course_year':course_year,
                                'course_division':course_division,
                                'course_subject':course_subject 
                        }
                        where={
                            "ClassRoom_id":classroom_id,    
                        }
                        update = au.update_classroom(classroom_id,course_name,course_year,course_division,course_subject)
                        return redirect('Subject') 

def EditSubject(request,id):
        classroom_details = ClassRoom.objects.filter(ClassRoom_id = id)
        course_details = Course.objects.all()
        context = {'details':course_details, 'method':"update",'classroom':classroom_details}
        return render(request, 'superadmin/EditSubject.html', context)

def Records(request):
        return render(request, 'superadmin/records.html')
def Upload(request):
        return render(request, 'superadmin/Upload.html')
def Year(request):
        return render(request, 'superadmin/Year.html')


# GENERATING STUDENT ACCOUNT 

def make_student_account(CsvFile,actype):
        db = client['AttendanceProject']
        if actype == "teacher":
                collection = db['api_teacher_table']
                data = []
                base = 'media/'
                FileWithLocation = base+str(CsvFile)
                with open(FileWithLocation) as f:
                        reader = csv.reader(f)
                        for i in reader:
                                dict1 = {'student_prn':i[0],'fname':"",'lname':"",'phone_number':"",'college_email':i[1],'password':i[0],'personal_email':"",'status':False}
                                data.append(dict1)
        
                collection.insert_many(data)

        elif actype == "student":    
                collection = db['api_student_table']
                data = []
                base = 'media/'
                FileWithLocation = base+str(CsvFile)
                with open(FileWithLocation) as f:
                        reader = csv.reader(f)
                        for i in reader:
                                dict1 = {'student_prn':i[0],'fname':"",'lname':"",'phone_number':"",'college_email':i[1],'password':i[0],'personal_email':"",'status':False}
                                data.append(dict1)
                collection.insert_many(data)

def student_account_generations(request):
        value = request.session.get('user')
        permission = au.check_if_allowed(value)
        if permission == True:
                redirect('UploadFiles')
                if request.method=="POST":
                        field_check =  request.POST.get("field_check")
                        file_csv = request.FILES["student_account"]
                        data = StudentAccounts.objects.create(field_check = field_check,student_account_file = file_csv)
                        data.save()
                        make_student_account(file_csv,field_check) 
                return render(request, 'superadmin/Upload.html')
        else:
             return redirect('Login')   

# GENERATING TEACHER ACCOUNTS

# def make_teacher_account(CsvFile):
#         db = client['AttendanceProject']
#         collection = db['api_teacher_table']
#         data = []
#         base = 'media/'
#         FileWithLocation = base+str(CsvFile)
#         with open(FileWithLocation) as f:
#                 reader = csv.reader(f)
#                 for i in reader:
#                         dict1 = {'teacher_prn':i[0],'fname':"",'lname':"",'phone_number':"",'college_email':i[1],'password':i[0],'personal_email':"",'status':False}
#                         data.append(dict1)
#         collection.insert_many(data)

# def teacher_account_generations(request):
#         value = request.session.get('user')
#         permission = au.check_if_allowed(value)
#         if permission == True:
#                 redirect('UploadFiles')
#                 if request.method=="POST":
#                         file_csv = request.FILES["teacher_account"]
#                         count = len(TeacherAccounts.objects.all()) + 1
#                         data = TeacherAccounts.objects.create(id = count,teacher_account_file = file_csv)
#                         data.save()
#                         make_teacher_account(file_csv) 
#                 return render(request, 'superadmin/UploadTeacher.html')
#         else:
#              return redirect('Login') 