from django.shortcuts import render
from .models import Servicio
# Create your views here.


def servicios_list(request):
    servicios = Servicio.objects.all()
    context = {
        'servicios': servicios,
        'subtitle': 'Lista de servicios'
    }
    return render(request, 'servicios.html', context)