from django.urls import path
from api import views

urlpatterns = [
    path('login/', views.Login),
    path('verify/', views.update_user_details),
    path('markattendance/', views.markattendance),
    path('getprofile/', views.getprofile),
    # Teacher APi
    path('teacher/login/', views.TeacherLogin),
    path('teacher/verify/', views.update_teacher_details),
]
