from django.contrib import admin
from apps.car.models import Category, Car, ImageCar


class CarImageAdmin(admin.ModelAdmin):
    list_display = ['car', 'image']
    list_filter = ['car']

admin.site.register(Category)
admin.site.register(Car)
admin.site.register(ImageCar, CarImageAdmin)