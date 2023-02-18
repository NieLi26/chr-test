from django.urls import path
from . import views
from test2.views import servicios_list

urlpatterns = [
    path('', views.station_list, name='stations'),
    path('networks/', views.network_list, name='networks'),
    path('companys/', views.company_list, name='companys'),
    path('payments/', views.payment_list, name='payments'),
    path('locations/', views.location_list, name='locations'),
    path('extras/', views.extra_list, name='extras'),
    path('servicios/', servicios_list, name='servicios'),
]