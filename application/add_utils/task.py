from application.models import Car, Location

def change_car_location():
    cars = Car.objects.all()
    for car in cars:
        random_location = Location.objects.order_by('?').first()
        car.current_location = random_location
        car.save()