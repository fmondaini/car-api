from django.contrib import admin
from .models import (
    Manufacturer,
    CarModel,
    Car,
    Service)


admin.site.register(Manufacturer)
admin.site.register(CarModel)
admin.site.register(Car)
admin.site.register(Service)
