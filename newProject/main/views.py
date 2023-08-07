from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def energysaving(request):
    return render(request, 'main/energysaving.html')


def energyefficiency(request):
    return render(request, 'main/energyefficiency.html')


def nuclearenergy(request):
    return render(request, 'main/nuclearenergy.html')


def nucencalc(request):

    if request.method == 'POST':
        m = int(request.POST.get('m'))
        c = int(request.POST.get('c'))
        result = m * c**2

    else:
        result = None

    context = {
        'result': result
    }

    return render(request, 'main/nucencalc.html', context)


def eneffcalc(request):

    if request.method == 'POST':
        q = int(request.POST.get('q'))
        w = int(request.POST.get('w'))
        result = q / w

    else:
        result = None

    context = {
        'result': result
    }

    return render(request, 'main/eneffcalc.html', context)


def ensavingcalc(request):

    if request.method == 'POST':
        Tc = int(request.POST.get('Tc'))
        Th = int(request.POST.get('Th'))
        result = 1 - (Tc / Th)

    else:
        result = None

    context = {
        'result': result
    }

    return render(request, 'main/ensavingcalc.html', context)
