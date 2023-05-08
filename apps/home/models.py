from django.db import models

from apps.user.models import User
from apps.home.services import get_upload_path, validate_file_extension
from apps.home.choices import *


class CategoryHome(models.Model):
    
    class Meta:
        db_table = 'category_home'
        verbose_name = 'Категория недвижимость'
        verbose_name_plural = 'Категория недвижимости'
        
    parent = models.ForeignKey('self', on_delete=models.PROTECT, related_name='children', blank=True, null=True)
    name = models.CharField(verbose_name="Название категории", max_length=255)
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    icon = models.FileField(upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class RealEstate(models.Model):
    
    class Meta:
        db_table = 'real_estate'
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'
        
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Заголовок объявления", max_length=128)
    seller_type = models.CharField(verbose_name="Тип продавца", max_length=100, default=None, choices=SellerType, blank=True, null=True)
    category = models.ForeignKey(CategoryHome, verbose_name="Категория", on_delete=models.CASCADE)
    address = models.CharField(verbose_name='Адрес', max_length=32)
    total_area = models.CharField(verbose_name="Общая площадь", max_length=128, blank=True, null=True)
    living_space = models.CharField(verbose_name="Жилая площадь", max_length=128, blank=True, null=True)
    floor = models.IntegerField(verbose_name='Этаж', blank=True, null=True)
    floor_home = models.IntegerField(verbose_name='Этажей в доме', blank=True, null=True)
    material = models.CharField(verbose_name="Выберите материал", max_length=100, default=None, choices=Material, blank=True, null=True)
    repair = models.CharField(verbose_name="Выберите тип ремонта", max_length=32, choices=Repair, default=None, blank=True, null=True)
    balcony = models.CharField(verbose_name="Выберите тип балкона", max_length=32, choices=Balcony, default=None, blank=True, null=True)
    bathroom = models.CharField(verbose_name="Выберите тип санузла", max_length=100, default=None, choices=Bathroom, blank=True, null=True)
    years = models.CharField(verbose_name="Год постройки", max_length=32, blank=True, null=True)
    parking = models.CharField(verbose_name="Выберите тип парковки", max_length=32, choices=Parking, default=None, blank=True, null=True)
    flat = models.IntegerField(verbose_name='Квартира', blank=True, null=True)
    entrance = models.IntegerField(verbose_name='Пподъезд', blank=True, null=True)
    house = models.IntegerField(verbose_name='Дом', blank=True, null=True)
    conditioning = models.BooleanField(verbose_name="Кондиционер", default=False)
    refrigerator = models.BooleanField(verbose_name="Холодильник", default=False)
    elevator = models.BooleanField(verbose_name="Лифт", default=False)
    security = models.BooleanField(verbose_name="Охрана", default=False)
    internet = models.BooleanField(verbose_name="Интернет", default=False)
    furniture = models.BooleanField(verbose_name="Мебель", default=False)
    consumer_electronics = models.BooleanField(verbose_name="Бытовая электроника", default=False)
    garbage_chute = models.BooleanField(verbose_name="Мусоропровод", default=False)
    description = models.TextField(verbose_name="Как можно подробнее опишите Ваш объект недвижимости", blank=True, null=True)
    price = models.BigIntegerField(verbose_name="Цена", blank=True, null=True)
    negotiable = models.BooleanField(verbose_name="Договорная", default=False)
    
    def __str__(self):
        return self.name
    
    
class ImageHome(models.Model):
    class Meta:
        db_table = 'home_image'
        verbose_name = 'фото'
        verbose_name_plural = 'фотографии'
    
    home = models.ForeignKey(RealEstate, verbose_name="Недвижимость", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фотография', upload_to='images/car')
    
    def __str__(self):
        return f'{self.home}'