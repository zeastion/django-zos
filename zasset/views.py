from django.shortcuts import render

from zasset.models import Hardware


def assetindex(request):

    return render(request, 'zasset/index.html',)


def hardware(request):

    hardware_list = Hardware.objects.order_by('owner')
    context_dict = {'hardwares': hardware_list}

    return render(request, 'zasset/hardware.html', context_dict)


def software(request):

    return render(request, 'zasset/software.html',)
