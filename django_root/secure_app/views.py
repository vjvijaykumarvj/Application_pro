from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from.models import Employee
from.serializer import EmployeeSeailizer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

class Employee_MVS(ModelViewSet):
    serializer_class = EmployeeSeailizer
    queryset = Employee.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

