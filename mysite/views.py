from django.http import HttpResponse
from django.shortcuts import render

from employess.models import employee


def home(request):
    # ambil semua data dari model Employee
    employees = employee.objects.all()
    # print(employees)
    context = {
        'employees': employees,
    }
    return render(request, 'home.html', context)
