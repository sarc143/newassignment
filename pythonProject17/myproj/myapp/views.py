from django.shortcuts import render
from .models import Employee
from typing import List, Dict

def all_employees(request):
    employees = Employee.objects.select_related('manager').all()

    context = {
        'employees': employees,
    }
    return render(request, 'all_employees.html', context)

def get_employee_hierarchy(employee: Employee) -> List[Dict]:
    employees = [{
        'id': employee.id,
        'first_name': employee.first_name,
        'last_name': employee.last_name,
        'title': employee.title,
        'manager_id': employee.manager.id if employee.manager else None,
        'manager_name': f'{employee.manager.first_name} {employee.manager.last_name}' if employee.manager else None
    }]
    for report in employee.direct_reports.all():
        employees.extend(get_employee_hierarchy(report))
    return employees

def manager_hierarchy(request, manager_id: int):
    manager = Employee.objects.select_related('manager').get(id=manager_id)
    hierarchy = get_employee_hierarchy(manager)

    context = {
        'manager': manager,
        'hierarchy': hierarchy,
    }
    return render(request, 'manager_hierarchy.html', context)
