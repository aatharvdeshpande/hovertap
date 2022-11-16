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