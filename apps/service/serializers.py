from rest_framework import serializers as s

from apps.service.models import CategoryService, Service, Comment
from apps.user.serializers import UserSerializer


class CategoryHomeSerializer(s.ModelSerializer):
    
    class Meta:
        model = CategoryHome
        fields = ['name', 'id']


class RealEstateSerializer(s.ModelSerializer):
    category_home = CategoryHomeSerializer()
    user = UserSerializer()
    
    class Meta:
        model = RealEstate
        fields = ['user', 'name', 'category', 'address', 'flat', 'entrance', 
                'floor', 'house', 'description', 'price', 'id']


class ImageHomeSerializer(s.ModelSerializer):
    home = RealEstateSerializer()

    class Meta:
        model = ImageHome
        fields = '__all__'