from rest_framework import generics
from .serializers import EmployeeSerializers
from .models import Employee

class EmployeeAPI(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = EmployeeSerializers
    queryset = Employee.objects.all()

class EmployeeDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializers
    queryset = Employee.objects.all()