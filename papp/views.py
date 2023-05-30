from django.shortcuts import render
from random import randint
from twilio.rest import Client
from django.http import JsonResponse
from .models import master_user
from .serializers import master_user_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import query
import time
from django.db import connection

# Create your views here.

@api_view(['GET','POST'])
def get_number(request):
    if request.method == 'GET':
        user_table = master_user.objects.all()
        serializer = master_user_serializer(user_table, many=True)
        return JsonResponse({'data':serializer.data})

    if request.method == 'POST':
        serializer = master_user_serializer(data=request.data)
        if serializer.is_valid():
            number = serializer.validated_data.get('user_m_no')
            user_name = serializer.validated_data.get('user_name')
            query.insert_data(number, user_name)
            # Generate OTP and timestamp
            otp = randint(1000, 9999)
            print(otp)
            timestamp = time.time()

            # Store the OTP and timestamp in session
            request.session['generated_otp'] = otp
            request.session['otp_timestamp'] = timestamp
            request.session['user_m_no'] = number

            # Send OTP via SMS
            account_sid = "AC46b86aa71d8f89805f08abf155f02607"
            auth_token = "3df788cb6cd0492960bfc8e9cde320ef"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"HELUU SAY'S HARSH: {otp}",
                from_='+13158649939',
                to=serializer.validated_data.get('user_m_no')
            )

            if message.sid:
                # Return success response
                return Response({'message': 'OTP sent successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Failed to send OTP via SMS."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def verify_otp(request):
    entered_otp = request.data.get('entered_otp')

    # Compare the entered OTP with the generated OTP
    if entered_otp == str(request.session.get('generated_otp')):
        # Check the time limit
        timestamp = request.session.get('otp_timestamp')
        current_time = time.time()
        time_limit = 30  # 30 seconds time limit

        if current_time - timestamp <= time_limit:
            # Update otp_status in the database for the corresponding user_m_no
            user_m_no = request.session.get('user_m_no')
            User_Name = query.get_user_name(user_m_no)
            update_status = query.update_otp_status(user_m_no)
            if update_status == 'True':
                return Response({'message': 'Welcome ' + User_Name}, status=status.HTTP_200_OK)
            else:
                query.delete_user(user_m_no)
                return Response({'message': 'Something went wrong'})
        else:
            user_m_no = request.session.get('user_m_no')
            query.delete_user(user_m_no)
            return Response({'message': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        user_m_no = request.session.get('user_m_no')
        query.delete_user(user_m_no)
        return Response({'message': 'Incorrect OTP'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def display_images(request):
    images = query.get_all_images()  # Use your PostgreSQL query function to retrieve all images
    response_data = []

    for image in images:
        image_data = {
            image['img'],
            image['img_name']
        }
        response_data.append(image_data)

        time.sleep(1)  # Delay for seconds

    print(response_data)
    return Response(response_data)


@api_view(['POST'])
def process_user_response(request):
    user_name = request.data.get('user_id')
    img_name = request.data.get('img_name')

    print(user_name, img_name)
    user_id = query.get_user_id(user_name)
    img_id = query.get_img_id(img_name)
    
    print(user_id,img_id)
    

    response = request.data.get('response')


    # Process the user's response (accept or reject)
    if response == 'accepted':
        # Handle image acceptance
        query.insert_transaction(user_id, img_id, 'true')
        message = f"User {user_id} accepted image {img_id}"
    elif response == 'rejected':
        # Handle image rejection
        query.insert_transaction(user_id, img_id, 'false')
        message = f"User {user_id} rejected image {img_id}"
    else:
        return Response({'message': 'Invalid response'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': message}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_image_info(request):
    # Please update id maually
    image_data = query.get_image_data(str(58)) 
    response_data = []
    
    for data in image_data:
        image_info = {
            'img_id': data['img_id'],
            'status': data['status']
        }
        print(image_info)
        response_data.append(image_info)
    
    return Response(response_data)