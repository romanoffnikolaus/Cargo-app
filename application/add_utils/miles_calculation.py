from geopy.distance import geodesic

from application.models import Car


class DistanceCalculator:
    @staticmethod
    def calculate_distance(coordinate1, coordinate2):
        return geodesic(coordinate1, coordinate2).miles

    @classmethod
    def calculation(cls, instance):
        pick_address = instance.pick_up
        pick_up_coordinate = (pick_address.latitude, pick_address.longitude)
        selected_cars = Car.objects.all()
        filtered_cars = list(filter(
            lambda car: cls.calculate_distance(pick_up_coordinate, (car.latitude, car.longitude)) <= 450,
            selected_cars
        ))
        return filtered_cars

    @classmethod
    def retrieve_calculation(cls, instance, pick_up):
        pick_up_coordinate = (pick_up.latitude, pick_up.longitude)
        cars = Car.objects.all()
        selected_cars = (
            {'car': car.unic_number, 'distance': cls.calculate_distance(pick_up_coordinate, (car.latitude, car.longitude))}
            for car in cars
        )
        return selected_cars

    @classmethod
    def filter_distance(cls, instance, max_distance):
        pick_up_coordinate = (instance.pick_up.latitude, instance.pick_up.longitude)
        selected_cars = Car.objects.all()
        filtered_cars = list(filter(
            lambda car: cls.calculate_distance(pick_up_coordinate, (car.latitude, car.longitude)) <= max_distance,
            selected_cars
        ))
        return filtered_cars


distance_calculator = DistanceCalculator()