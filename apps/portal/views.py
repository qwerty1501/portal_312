from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.portal.models import Category, Product, ImageProd, BannerOne, BannerTwo, BannerThree, BannerFour, News
from apps.portal.serializers import CategorySerializer, ProductSerializer, ImageProdSerializer, BannerOneSerializer, BannerTwoSerializer, BannerThreeSerializer, BannerFourSerializer, NewsSerializer

# CATEGORY
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
# PRODUCT
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['name', 'category_car', 'price']
    search_fields = ['name', 'price']
    
    
class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['name', 'category_car', 'price']
    search_fields = ['name', 'price']
    
# IMAGE_PROD 
class ImageProdListAPIView(ListAPIView):
    queryset = ImageProd.objects.all()
    serializer_class = ImageProdSerializer
    
    
class ImageProdRetrieveAPIView(RetrieveAPIView):
    queryset = ImageProd.objects.all()
    serializer_class = ImageProdSerializer

    
# BANNER_ONE
class BannerOneListAPIView(ListAPIView):
    queryset = BannerOne.objects.all()
    serializer_class = BannerOneSerializer

# BANNER_TWO
class BannerTwoListAPIView(ListAPIView):
    queryset = BannerTwo.objects.all()
    serializer_class = BannerTwoSerializer
    
# BANNER_THREE
class BannerThreeListAPIView(ListAPIView):
    queryset = BannerThree.objects.all()
    serializer_class = BannerThreeSerializer
    
# BANNER_FOUR
class BannerFourListAPIView(ListAPIView):
    queryset = BannerFour.objects.all()
    serializer_class = BannerFourSerializer
    
# NEWS
class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer