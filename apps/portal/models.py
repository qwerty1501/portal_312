from django.db import models
from colorfield.fields import ColorField

from apps.portal.choices import State
from apps.user.models import User


class Category(models.Model):
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    logo = models.ImageField(verbose_name='Фотография', upload_to='images/logo/prod')
    name = models.CharField(verbose_name="Категория", max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=128)
    state = models.CharField(verbose_name="Состояние", max_length=100, default=None, choices=State, blank=True, null=True)
    color = ColorField(default='#FF0000')
    size = models.CharField(verbose_name="Размер", max_length=128, blank=True, null=True)
    price = models.BigIntegerField(verbose_name="Цена", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class ImageProd(models.Model):
    
    class Meta:
        db_table = 'prod_image'
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фотографии продукта'
        
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)
    images = models.ImageField(verbose_name='Фотография', upload_to='images/prod')
    
    
class BannerOne(models.Model):
    class Meta:
        db_table = 'banner_one'
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры_1'
    
    name = models.CharField(verbose_name="Название", max_length=64)
    images = models.ImageField(verbose_name="Фотография: *pекомендация(1440x530)", upload_to='images/bannre')
    url = models.URLField(verbose_name="Укажите url ссылку", max_length=200)
    
    def __str__(self):
        return self.name
    
    
class BannerTwo(models.Model):
    class Meta:
        db_table = 'banner_two'
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры_2'
    
    name = models.CharField(verbose_name="Название", max_length=64)
    images = models.ImageField(verbose_name="Фотография: *pекомендация(1440x530)", upload_to='images/bannre')
    url = models.URLField(verbose_name="Укажите url ссылку", max_length=200)
    
    def __str__(self):
        return self.name
    
    
class BannerThree(models.Model):
    class Meta:
        db_table = 'banner_three'
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры_3'
    
    name = models.CharField(verbose_name="Название", max_length=64)
    images = models.ImageField(verbose_name="Фотография: *pекомендация(1440x530)", upload_to='images/bannre')
    url = models.URLField(verbose_name="Укажите url ссылку", max_length=200)
    
    def __str__(self):
        return self.name
    
    
class BannerFour(models.Model):
    class Meta:
        db_table = 'banner_four'
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры_4'
    
    name = models.CharField(verbose_name="Название", max_length=64)
    images = models.ImageField(verbose_name="Фотография: *pекомендация(1440x530)", upload_to='images/bannre')
    url = models.URLField(verbose_name="Укажите url ссылку", max_length=200)
    
    def __str__(self):
        return self.name
    
    
class News(models.Model):
    
    class Meta:
        db_table = ''
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Заголовок", max_length=128)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    created = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True, blank=True)
    approved = models.BooleanField(verbose_name="Одобренный", default=False)
    
    def __str__(self):
        return self.title