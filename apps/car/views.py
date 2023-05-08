from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.car.models import Category, Car, ImageCar
from apps.car.serializers import CarSerializer, ImageCarSerializer, CategoryCarSerializer

# CAR CATEGORY
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True). \
        select_related('parent'). \
        prefetch_related('children',
                         'children__children',
                         'children__children__children')
    serializer_class = CategoryCarSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class CategoryRetrieve(generics.RetrieveAPIView):
    queryset = Category.objects.filter()

    serializer_class = CategoryCarSerializer
    
# CAR
class CarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['name', 'category_car', 'price']
    search_fields = ['name', 'price']
    
    
class CarDeleteView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # filter_backends = [SearchFilter, DjangoFilterBackend]
    # filter_fields = ['name', 'category_car', 'price']
    # search_fields = ['name', 'price']
    
# CAR IMAGE 
class ImageCarListAPIView(ListAPIView):
    queryset = ImageCar.objects.all()
    serializer_class = ImageCarSerializer
    
    
class ImageCarRetrieveAPIView(RetrieveAPIView):
    queryset = ImageCar.objects.all()
    serializer_class = ImageCarSerializer