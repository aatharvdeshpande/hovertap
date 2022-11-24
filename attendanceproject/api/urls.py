from django.urls import path
from api import views

urlpatterns = [
    path('login/', views.Login),
    path('verify/', views.update_user_details),
]
