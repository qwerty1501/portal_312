from rest_framework import serializers as s

from apps.home.models import CategoryHome, RealEstate, ImageHome
from apps.user.serializers import UserSerializer


class RecursiveHomeSerializer(s.Serializer):
    
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoryHomeSerializer(s.ModelSerializer):
    children = RecursiveHomeSerializer(many=True)

    class Meta:
        model = CategoryHome
        fields = ['id', 'name', 'icon', 'image', 'children']


class RealEstateSerializer(s.ModelSerializer):
    category = CategoryHomeSerializer()
    user = UserSerializer()
    
    class Meta:
        model = RealEstate
        fields = ['user', 'name', 'category', 'address', 'total_area',
                'living_space', 'floor', 'floor_home', 'material', 'repair',
                'balcony', 'bathroom', 'years', 'parking', 'flat', 'entrance', 
                'floor', 'house', 'conditioning', 'refrigerator', 'elevator',
                'security', 'internet', 'furniture', 'consumer_electronics',
                'garbage_chute', 'description', 'price', 'id']


class ImageHomeSerializer(s.ModelSerializer):
    home = RealEstateSerializer()

    class Meta:
        model = ImageHome
        fields = '__all__'