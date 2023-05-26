from django.db import models
from django.db.models import JSONField
from django.core.validators import MaxValueValidator, MinValueValidator

from .add_utils.code_generator import generate_car_code


class Location(models.Model):
    """Класс локаций"""

    zip_code = models.PositiveIntegerField(primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=5)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)
    city = models.CharField(max_length=40, blank=False)
    state_id = models.CharField(max_length=3, blank=False)
    state_name = models.CharField(max_length=40, blank=False)
    zcta = models.BooleanField(blank=False)
    parent_zcta = models.CharField(blank=True, null=True)
    population = models.PositiveIntegerField(blank=True, null=True)
    density = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    county_fips = models.PositiveIntegerField(blank=False)
    county_name = models.CharField(max_length=45, blank=False)
    county_weights = JSONField()
    county_names_all = models.CharField(max_length=150, blank=False)
    county_fips_all = models.CharField(max_length=60, blank=True)
    imprecise = models.BooleanField(blank=False)
    military = models.BooleanField(blank=False)
    timezone = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f'{self.zip_code} - {self.city}'
    
    class Meta:
        indexes = [models.Index(fields=['zip_code']),]
    

class Cargo(models.Model):
    """Класс грузов"""

    pick_up = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, related_name='pick_up')
    delivery = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, related_name='delivery')
    weight = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1000),MinValueValidator(1)])
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'cargo id: {self.id}: {self.pick_up} to {self.delivery}'

    class Meta:
        indexes = [models.Index(fields=['pick_up']),]


class Car(models.Model):
    """Класс транспорта"""

    unic_number = models.CharField(max_length=5, blank=True, primary_key=True)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, related_name='current_location')
    capacity = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1000),MinValueValidator(1)])
    latitude = models.DecimalField(max_digits=9, decimal_places=5, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=5, blank=True, null=True)

    def __str__(self):
        return f'unic_number: {self.unic_number}'

    def save(self, *args, **kwargs):
        if not self.current_location_id:
            random_location = Location.objects.order_by('?').first()
            self.current_location = random_location
        if not self.unic_number:
            self.unic_number = generate_car_code()
        if self.current_location:
            self.latitude = self.current_location.latitude
            self.longitude = self.current_location.longitude
        super().save(*args, **kwargs)
    
    class Meta:
        indexes = [models.Index(fields=['latitude', 'longitude']),]