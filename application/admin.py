from django.contrib import admin

from .models import Location, Car, Cargo


class LocationAdmin(admin.ModelAdmin):
    list_display = ('zip_code', 'city', 'state_name', 'county_name')

class CargoAdmin(admin.ModelAdmin):
    list_display = ('pick_up', 'delivery', 'weight', 'description')

class CarAdmin(admin.ModelAdmin):
    list_display = ('unic_number', 'current_location', 'latitude', 'longitude', 'capacity')


admin.site.register(Cargo, CargoAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Location, LocationAdmin)

