from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('AdminHome/', views.AdminHome, name = "AdminHome"),
    path('UploadFiles/', views.SaveData, name = "UploadFiles"),
    path('SaveData/', views.SaveData, name = "SaveData"),
    path('ViewStudents/', views.ShowAccounts, name = "ViewStudents"),
    path('Login/', views.Login, name = "Login"),
    path('ForgotPassword/', views.ForgotPassword, name = "ForgotPassword"),
    path('SignUp/', views.SignUp, name = "SignUp"),
    path('AddCourse/', views.AddCourse, name = "AddCourse"),
    path('ShowAllCourse/', views.ShowAllCourse, name = "ShowAllCourse"),
    path('division/', views.division, name = "division"),
    path('AddDivision/', views.AddDivision, name = "AddDivision"),
    path('AddYear/', views.AddYear, name = "AddYear"),
    path('AddSubject/', views.AddSubject, name = "AddSubject"),
    path('year/', views.year, name = "year"),
    path('subject/', views.subject, name = "subject"),
    path('Course/', views.course, name = "course" )
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
