from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm


def EmployeeDashboard(request):
    if request.method == 'GET':
        emp_list = Employee.objects.all()
        emp_form = EmployeeForm()
        emp_dict = {
            'emp_list': emp_list,
            'emp_form': emp_form
        }
        return render(request, 'Emp_MVS_app/emp_dshboard.html', context=emp_dict)
    elif request.method == 'POST':
        emp_form = EmployeeForm(request.POST, request.FILES)
        if emp_form.is_valid():
            emp_form.save()

        # name = request.POST.get('name')
        # age =  request.POST.get('age')
        # salary =  request.POST.get('salary')
        # address =  request.POST.get('address')
        # photo =  request.POST.get('photo')
        # pincode =  request.POST.get('pincode')
        # mobile =  request.POST.get('mobile')
        # pancard =  request.POST.get('pancard')
        # employee = Employee(name=name,age=age,salary=salary,address=address,pincode=pincode,pancard=pancard,photo=photo,mobile=mobile)
        # employee.save()
        return redirect('/employee_dashboard/')


def employee_update(request, pk):
    if request.method == 'GET':
        emp_list = Employee.objects.all()
        employee_db = Employee.objects.get(id=pk)
        emp_form = EmployeeForm(instance=employee_db)
        emp_dict = {
            'emp_list': emp_list,
            'emp_form': emp_form,
            'employee': employee_db,
            'is_updated': 'yes'
        }
        return render(request, 'Emp_MVS_app/emp_dshboard.html', context=emp_dict)
    elif request.method == 'POST':
        employee = Employee.objects.get(id=pk)
        emp_form = EmployeeForm(request.POST, request.FILES,instance=employee)
        if emp_form.is_valid():
            emp_form.save()
        return redirect('/employee_dashboard/')


def employee_delete(request, pk):
    employee_db = Employee.objects.get(id=pk)
    employee_db.delete()
    return redirect('/employee_dashboard/')
