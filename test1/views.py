from django.shortcuts import render

from .models import (
    Station, Location,
    Network, Company,
    Payment, Extra
)


def station_list(request):
    stations = Station.objects.all()
    context = {
        'stations': stations,
        'subtitle': 'Lista de estaciones',
    }
    return render(request, 'stations.html', context)


def company_list(request):
    companys = Company.objects.all()
    context = {
        'companys': companys,
        'subtitle': 'Lista de compañias'
    }
    return render(request, 'companys.html', context)


def network_list(request):
    networks = Network.objects.all()
    context = {
        'networks': networks,
        'subtitle': 'Lista de redes',
    }
    return render(request, 'networks.html', context)


def payment_list(request):
    payments = Payment.objects.all()
    context = {
        'payments': payments,
        'subtitle': 'Lista de pagos',
    }
    return render(request, 'payments.html', context)


def location_list(request):
    locations = Location.objects.all()
    context = {
        'locations': locations,
        'subtitle': 'Lista de locaciones',
    }
    return render(request, 'locations.html', context)


def extra_list(request):
    extras = Extra.objects.all()
    context = {
        'extras': extras,
        'subtitle': 'Lista de extras',
    }
    return render(request, 'extras.html', context)

