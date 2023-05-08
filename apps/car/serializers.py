from rest_framework import serializers as s

from apps.car.models import Category, Car, ImageCar


class RecursiveSerializer(s.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoryCarSerializer(s.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'image', 'children']


class CarSerializer(s.ModelSerializer):
    category_car = CategoryCarSerializer()
    
    class Meta:
        model = Car
        fields = ['category_car', 'name', 'new', 'color', 'body_car', 'engine',
                'volume', 'transmission', 'mileage', 'drive_unit', 'steering_wheel', 'steering_wheel',
                'pts', 'year', 'price', 'state', 'description', 'address', 'id']


class ImageCarSerializer(s.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = ImageCar
        fields = '__all__'