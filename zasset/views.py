from django.shortcuts import render

from zasset.models import Department, Staff, Hardware

def zstaffindex(request):
    return render(request, 'zasset/staffindex.html', )


def zstaff(request):

    staff_list = Staff.objects.order_by('sname')
    context_dict = {'staffs': staff_list}

    return render(request, 'zasset/staff.html', context_dict)


def zdepartment(request):

    department_list = Department.objects.order_by('dname')
    context_dict = {'departments': department_list}

    return render(request, 'zasset/department.html', context_dict)

def zassetindex(request):

    return render(request, 'zasset/assetindex.html',)


def hardware(request):

    hardware_list = Hardware.objects.order_by('staff')
    context_dict = {'hardwares': hardware_list}

    return render(request, 'zasset/hardware.html', context_dict)


def software(request):

    return render(request, 'zasset/software.html',)
