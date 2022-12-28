from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from.models import Employee
from.serializer import Employee_Serializer

class Employee_Validate(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializer