from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        abstract = True


class Manufacturer(TimeStampedModel):
    name = models.CharField(max_length=50)
    # logo

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"


class CarModel(TimeStampedModel):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    manufacturer = models.ForeignKey('Manufacturer')

    class Meta:
        verbose_name = "CarModel"
        verbose_name_plural = "CarModels"

    def __str__(self):
        return "{manufacturer} {name} / {year}".format(
            manufacturer=self.manufacturer,
            name=self.name,
            year=self.year
        )


class Car(TimeStampedModel):
    name = models.CharField(max_length=50)
    # vin
    # odometer = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    # get_odometer_in_miles
    # get_odometer_in_km


class Service(TimeStampedModel):
    car = models.ForeignKey('Car')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    # odometer  # Caso não seja preenchido, pegar odometro atual.
    replaced_parts = models.TextField()
    # periodic?

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
