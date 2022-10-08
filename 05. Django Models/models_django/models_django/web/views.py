from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from models_django.web.models import Employee, Department, Project


def index(request):
    employees = Employee.objects.all()
    # employees = [e for e in Employee.objects.all() if e.department_id == 4]
    # employees2 = Employee.objects.filter(department_id=2) \
    employees2 = Employee.objects.filter(department__name='Engineering') \
        .order_by('first_name', 'last_name')  # .filter(age__range=18-20) \

    department = Department.objects.get(pk=2)  # `get` returns an object not a QuerySet
    # `get` returns a single object and throws when none or multiple results
    # get_object_or_404(Employee, age=43)

    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }

    return render(request, 'index.html', context)

    # employees = Employee.objects.all()  # objects <- Manager
    # # `employees` is empty QuerySet, is not executed
    # # QuerySet - lazy structure, it is executed when s.o. wants to execute it
    # employees_list = list(employees)
    # print(list(User.objects.all()))
    # print(list(Department.objects.all()))
    # print(employees) # <QuerySet [<Employee: Id: 5; Name: Anna Ivanova>, <Employee: Id: 6; Name: Georgi Georgiev>]>


def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug)
    }

    return render(request, 'department-details.html', context)


def delete_employee(request, pk):
    # department_pk = 3
    ## When `Restricted` this must be done explicitly
    ## When `Cascade` this is done implicitly
    # Employee.objects.filter(department_id=department_pk) \
    #     .delete()

    # get_object_or_404(Department, pk=1).delete()
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    # Project.objects.all().delete() ## delete all
    # Project.objects.filter().delete() ## delete filtered
    return redirect('index')
