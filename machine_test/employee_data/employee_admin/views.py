from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse

def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        position = request.POST['position']
        salary = request.POST['salary']
        Employee.objects.create(name=name, position=position, salary=salary)
        return redirect('display')
    return render(request, 'add_employee.html')

def remove_employee(request, emp_id):
    Employee.objects.filter(id=emp_id).delete()
    return redirect('display')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee

def remove_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    
    if request.method == 'POST':
        emp.delete()
        return redirect('view_employees')
    
    return render(request, 'remove_employee.html', {'employee': emp})


def promote_employee(request, emp_id):
    if request.method == 'POST':
        increment = int(request.POST['increment'])
        emp = Employee.objects.get(id=emp_id)
        emp.salary += increment
        emp.save()
        return redirect('display')  # or 'view_employees' based on your flow
    return render(request, 'promote_employee.html', {'id': emp_id})



def display_employees(request):
    employees = Employee.objects.all()
    return render(request, 'display.html', {'employees': employees})
    

def home(request):
    return render(request, 'employee_admin/home.html')

def dashboard(request):
    return render(request, 'employee_admin/dashboard.html')

def view_employees(request):
    return render(request, 'employee_admin/view_employees.html')

