from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import api.authenticate_user as au
import json
# Create your views here.
@api_view(['GET', 'POST'])
def Login(request):
    a = request.data
    username = a['email']
    password = a['password']
    data = au.auth_user(username,password)
    return  Response(data, status=status.HTTP_200_OK) 

@api_view(['GET', 'POST'])
def update_user_details(request):
    a = request.data
    student_prn = a['student_prn']
    fname = a['fname']
    lname = a['lname']
    phone_number = a['phone_number']
    personal_email = a['personal_email']
    data = au.update_user(student_prn,fname,lname,phone_number,personal_email)
    return  Response(data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def markattendance(request):
    a = request.data
    student_prn = a['student_prn']
    nfcid = a['nfcid']
    date = a['date']
    time = a['time']
    data = au.markAttendance(student_prn,nfcid,date,time)
    return  Response(data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def getprofile(request):
    a = request.data
    student_prn = a['student_prn']
    data = au.getuserprofile(student_prn)
    return  Response(data, status=status.HTTP_200_OK)  

@api_view(['GET', 'POST'])
def update_user_profile(request):
    a = request.data
    student_prn = a['student_prn']
    fname = a['fname']
    lname = a['lname']
    phone_number = a['phone_number']
    personal_email = a['personal_email']
    data = au.update_user(student_prn,fname,lname,phone_number,personal_email)
    return  Response(data, status=status.HTTP_200_OK)     

@api_view(['GET', 'POST'])
def update_password(request):
    a = request.data
    student_prn = a['student_prn']
    password = a['password']
    data = au.update_password(student_prn,password)
    return  Response(data, status=status.HTTP_200_OK)     

@api_view(['GET', 'POST'])
def getUserTimeTable(request):
    a = request.data
    student_prn = a['student_prn']
    time = a['time']
    day = a['day']
    data = au.get_user_timetable(student_prn,time,day)
    return  Response(data, status=status.HTTP_200_OK) 


# Teacher API
@api_view(['GET', 'POST'])
def TeacherLogin(request):
    a = request.data
    username = a['email']
    password = a['password']
    data = au.auth_teacher(username,password)
    return  Response(data, status=status.HTTP_200_OK) 

@api_view(['GET', 'POST'])
def update_teacher_details(request):
    a = request.data
    teacher_prn = a['teacher_prn']
    fname = a['fname']
    lname = a['lname']
    phone_number = a['phone_number']
    personal_email = a['personal_email']
    data = au.update_teacher(teacher_prn,fname,lname,phone_number,personal_email)
    return  Response(data, status=status.HTTP_200_OK)         

@api_view(['GET', 'POST'])
def getteacherprofile(request):
    a = request.data
    teacher_prn = a['teacher_prn']
    data = au.getteacherprofiles(teacher_prn)
    return  Response(data, status=status.HTTP_200_OK)  

@api_view(['GET', 'POST'])
def update_teacher_profile(request):
    a = request.data
    teacher_prn = a['teacher_prn']
    fname = a['fname']
    lname = a['lname']
    phone_number = a['phone_number']
    personal_email = a['personal_email']
    data = au.update_teacher(teacher_prn,fname,lname,phone_number,personal_email)
    return  Response(data, status=status.HTTP_200_OK)     

@api_view(['GET', 'POST'])
def update_teacher_password(request):
    a = request.data
    teacher_prn = a['teacher_prn']
    password = a['password']
    data = au.update_teacher_password(teacher_prn,password)
    return  Response(data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def getsubject(request):
    a = request.data
    teacher_prn = a['teacher_prn']
    data = au.get_subject(teacher_prn)
    return  Response(data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def teachermarkattendance(request):
    a = request.data
    teacher_prn = a['teacher_prn']
    nfcid = a['nfcid']
    subject = a['subject']
    date = a['date']
    time = a['time']
    data = au.TmarkAttendance(teacher_prn,nfcid,subject,date,time)
    return  Response(data, status=status.HTTP_200_OK)    