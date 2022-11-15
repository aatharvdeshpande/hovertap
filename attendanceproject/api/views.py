from .models import Students
from .seralizers import StudentSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

class StudentList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
