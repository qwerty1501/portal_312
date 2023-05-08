from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.home.models import CategoryHome, RealEstate, ImageHome
from apps.home.serializers import CategoryHomeSerializer, RealEstateSerializer, ImageHomeSerializer

# Home CATEGORY
class CategoryHomeListAPIView(ListAPIView):
    queryset = CategoryHome.objects.all()
    serializer_class = CategoryHomeSerializer
    
    
class CategoryHomeRetriveAPIView(RetrieveAPIView):
    queryset = CategoryHome.objects.all()
    serializer_class = CategoryHomeSerializer
    
# HOME
class RealEstateListCreateAPIView(generics.ListCreateAPIView):
    queryset = RealEstate.objects.all()
    serializer_class = RealEstateSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['name', 'category', 'price']
    search_fields = ['name', 'price']
    
    
class RealEstateUpdateView(generics.UpdateAPIView):
    queryset = RealEstate.objects.all()
    serializer_class = RealEstateSerializer
    
    
class RealEstateDeleteView(generics.DestroyAPIView):
    queryset = RealEstate.objects.all()
    serializer_class = RealEstateSerializer

    
# IMAGE 
class ImageHomeListAPIView(ListAPIView):
    queryset = ImageHome.objects.all()
    serializer_class = ImageHomeSerializer
    
    
class ImageHomeRetrieveAPIView(RetrieveAPIView):
    queryset = ImageHome.objects.all()
    serializer_class = ImageHomeSerializer