from django.core.management.base import BaseCommand

from application.add_utils.code_generator import generate_car_code
from application.models import Location, Car


class Command(BaseCommand):
    help = 'Создание 20 машин'

    def handle(self, *args, **kwargs):
        locations = Location.objects.all()
        for i in range(20):
            random_location = locations.order_by('?').first()
            unic_number = generate_car_code()
            car = Car.objects.create(unic_number=unic_number, current_location=random_location, capacity=1000)
        self.stdout.write(self.style.SUCCESS('Successfully created 20 Car objects'))