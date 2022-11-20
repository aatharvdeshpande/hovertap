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
    path('Division/', views.Division, name = "Division"),
    path('Year/', views.Year, name = "Year"),
    path('Upload/', views.Upload, name = "Upload"),
    path('AddSubject/', views.AddSubject, name = "AddSubject"),
    path('Records/', views.Records, name = "Records"),
    path('Subject/', views.Subject, name = "Subject"),
    path('check/', views.check, name = "check"),
    path('ViewCourse/', views.ViewCourse, name = "ViewCourse"),
    path("EditCourse/<int:id>", views.EditCourse, name='EditCourse'),
    path("EditSubject/<int:id>", views.EditSubject, name='EditSubject'),
# Index page URLs
    path('', views.Home, name = "Home"), 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
