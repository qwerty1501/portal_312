from rest_framework import serializers as s

from apps.portal.models import Category, Product, ImageProd, BannerOne, BannerTwo, BannerThree, BannerFour, News


class CategorySerializer(s.ModelSerializer):
    class Meta:
        model = Category
        fields = ['logo', 'name', 'id']


class ProductSerializer(s.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = ['category', 'name', 'state', 'color', 'size', 'price', 'description', 'id']


class ImageProdSerializer(s.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ImageProd
        fields = '__all__'
        

class BannerOneSerializer(s.ModelSerializer):
    
    class Meta:
        model = BannerOne
        fields = '__all__'


class BannerTwoSerializer(s.ModelSerializer):
    
    class Meta:
        model = BannerTwo
        fields = '__all__'
        

class BannerThreeSerializer(s.ModelSerializer):
    
    class Meta:
        model = BannerThree
        fields = '__all__'


class BannerFourSerializer(s.ModelSerializer):
    
    class Meta:
        model = BannerFour
        fields = '__all__'
        
        
class NewsSerializer(s.ModelSerializer):
    
    class Meta:
        model = News
        fields = '__all__'