from django.urls import path
from api import views

urlpatterns = [
    path('login/', views.Login),
    path('verify/', views.update_user_details),
    path('markattendance/', views.markattendance),
    path('getprofile/', views.getprofile),
    path('updateprofile/', views.update_user_profile),
    path('updatepassword/', views.update_password),
    path('getusertimetable/', views.getUserTimeTable),
    # Teacher APi
    path('teacher/login/', views.TeacherLogin),
    path('teacher/verify/', views.update_teacher_details),
    path('teacher/getprofile/', views.getteacherprofile),
    path('teacher/updateprofile/', views.update_teacher_profile),
    path('teacher/updatepassword/', views.update_teacher_password),
    path('teacher/getsubject/', views.getsubject),
    path('teacher/markattendance/', views.teachermarkattendance),
    path('teacher/displayCount/', views.displayCount),
]
