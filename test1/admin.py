from django.contrib import admin
from .models import (
    Network, Payment, Location,
    Company, Extra, Station
)

# Register your models here.
admin.site.register(Network)
admin.site.register(Payment)
admin.site.register(Location)
admin.site.register(Company)
admin.site.register(Extra)
admin.site.register(Station)