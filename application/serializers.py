from rest_framework import serializers
from geopy.distance import great_circle as GC

from .models import Cargo, Location, Car
# from .add_utils.miles_calculation import calculation, filter_distance, retrieve_calculation
from .add_utils.miles_calculation import distance_calculator


class CargoSerilaizer(serializers.ModelSerializer):
    pick_up_zip = serializers.IntegerField(write_only=True)
    delivery_zip = serializers.IntegerField(write_only=True)

    class Meta:
        model = Cargo
        fields = ['id', 'pick_up', 'delivery', 'pick_up_zip', 'delivery_zip', 'weight', 'description', 'active']

    def create(self, validated_data):
        pick_up_zip = validated_data.pop('pick_up_zip')
        delivery_zip = validated_data.pop('delivery_zip')
        pick_up = Location.objects.get(zip_code=pick_up_zip)
        delivery = Location.objects.get(zip_code=delivery_zip)
        cargo = Cargo.objects.create(pick_up=pick_up, delivery=delivery, **validated_data)
        return cargo
    

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CargoListSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

    def to_representation(self, instance):
        representatioin = super().to_representation(instance)
        max_distance = self.context.get('max_distance')
        representatioin['Машины на расстоянии менее 450 миль от груза'] = CarSerializer(distance_calculator.calculation(instance), many = True).data
        if max_distance:
            representatioin[f'Машины на указанном расстоянии {max_distance}'] = CarSerializer(distance_calculator.filter_distance(instance, max_distance), many = True).data
        return representatioin
    
    
class CargoDetailSerializer(serializers.ModelSerializer):
    cars = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = '__all__'

    def get_cars(self, instance):
        pick_up = instance.pick_up
        cars = distance_calculator.retrieve_calculation(instance, pick_up)
        return [{'unic_number': car['car'], 'distance': car['distance']} for car in cars]


class CargoListFilterSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'