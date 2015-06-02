from django.shortcuts import render

from zstaff.models import Staff, Department

def zstaffindex(request):
    return render(request, 'zstaff/index.html', )


def zstaff(request):

    staff_list = Staff.objects.order_by('sname')
    context_dict = {'staffs': staff_list}

    return render(request, 'zstaff/staff.html', context_dict)


def zdepartment(request):

    department_list = Department.objects.order_by('dname')
    context_dict = {'departments': department_list}

    return render(request, 'zstaff/department.html', context_dict)