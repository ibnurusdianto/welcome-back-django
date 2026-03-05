from django.shortcuts import render, get_object_or_404
from employess.models import employee
from django.http import Http404

def employee_detail(request, pk):
    emp = get_object_or_404(employee, pk=pk)
    context = {'employee': emp}
    return render(request, 'employee_detail.html', context)

