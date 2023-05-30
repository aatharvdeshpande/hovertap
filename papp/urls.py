from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('GetMobileNumber/', views.get_number, name = "GetMobileNumber"),
    path('GetOtp/', views.verify_otp, name = "GetOtp"),
    path('DisplayImages/', views.display_images, name = "DisplayImages"),
    path('ProcessUserResponse/', views.process_user_response, name='ProcessUserResponse'),
    path('GetImageInfo/', views.get_image_info, name='GetImageInfo')
]