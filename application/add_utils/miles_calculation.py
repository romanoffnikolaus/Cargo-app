from geopy.distance import great_circle as GC

from application.models import Car


def calculation(instance):
    pick_adress = instance.pick_up
    latitude = pick_adress.latitude
    longitude = pick_adress.longitude
    pick_up_coordinate = (latitude, longitude)
    selected_cars = Car.objects.all().select_related('current_location') 
    filtered_cars = [car for car in selected_cars if GC(pick_up_coordinate, (car.current_location.latitude, car.current_location.longitude)).miles <= 450]
    return filtered_cars

def retrieve_calculation(instance, pick_up):
    latitude = pick_up.latitude
    longitude = pick_up.longitude
    pick_up_coordinate = (latitude, longitude)
    cars = Car.objects.all()
    selected_cars = []
    for car in cars:
        car_latitude = car.current_location.latitude
        car_longitude = car.current_location.longitude
        car_coordinate = (car_latitude, car_longitude)
        distance = GC(pick_up_coordinate, car_coordinate).miles
        selected_cars.append({'car': car.unic_number,'distance': distance})
    return selected_cars