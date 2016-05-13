# -*- coding: utf-8 -*-
from rest_framework import viewsets

from .models import (
    Manufacturer,
    CarModel,
    Car,
    Service,
)
from .serializers import (
    ManufacturerSerializer,
    CarModelSerializer,
    CarSerializer,
    ServiceSerializer,
)

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
