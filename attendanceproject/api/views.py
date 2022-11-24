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