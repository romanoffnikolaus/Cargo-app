from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
import django_filters
from rest_framework import filters

from . import serializers, models
from .add_utils.miles_calculation import retrieve_calculation



class CargoViewSet(ModelViewSet):
    queryset = models.Cargo.objects.all()
    serializer_class = serializers.CargoSerilaizer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.OrderingFilter]
    filterset_fields = ['weight',]
    ordering_fields = ['weight',]
    

    @swagger_auto_schema(tags=['Просмотр грузов и машин на расстоянии не более 450 миль'])
    def list(self, request, *args, **kwargs):
        max_distance = self.request.query_params.get('max_distance')
        if max_distance:
            queryset = self.get_queryset()
            serializer = serializers.CargoListSerialiser(queryset, many=True, context={'max_distance': float(max_distance)})
            return Response(serializer.data)
        else:
            self.serializer_class = serializers.CargoListSerialiser
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=['Просмотр груза и машин с расстоянием до точки груза + фильтр'])
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        pick_up = instance.pick_up
        cars = retrieve_calculation(instance, pick_up)
        serializer = serializers.CargoDetailSerializer(instance, context={'cars': cars})
        return Response(serializer.data)
