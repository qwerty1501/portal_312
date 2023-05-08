from colorfield.fields import ColorField
from django.db import models

from apps.portal.models import Category
from apps.car.services import get_upload_path, validate_file_extension
from apps.car.choices import BodyCar, Engine, State, Transmission, SteeringWheel, DriveUnit, Pts


class Category(models.Model):
    class Meta:
        db_table = 'categorycar'
        verbose_name = 'Категория машин'
        verbose_name_plural = 'Категории машин'
        
    parent = models.ForeignKey('self', on_delete=models.PROTECT, related_name='children', blank=True, null=True)
    name = models.CharField(verbose_name="Название категории", max_length=255)
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    icon = models.FileField(upload_to=get_upload_path, validators=[validate_file_extension], null=True, blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
    
    
class Car(models.Model):
    class Meta:
        db_table = 'car'
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
    
    category_car = models.ForeignKey(Category, verbose_name='Марка автомобиля', on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название автомобиля", max_length=200)
    new = models.BooleanField(verbose_name="Новый автомобиль", default=False)
    color = ColorField(default='#FF0000')
    body_car = models.CharField(verbose_name="Тип кузова", max_length=100, default=None, choices=BodyCar, blank=True, null=True)
    engine = models.CharField(verbose_name="Тип двигателя", max_length=100, default=None, choices=Engine, blank=True, null=True)
    volume = models.BigIntegerField(verbose_name="Объем двигателя", blank=True, null=True)
    engine_power = models.CharField(verbose_name="Мощность двигателя", max_length=32, blank=True, null=True)
    transmission = models.CharField(verbose_name="Коробка передач", max_length=100, default=None, choices=Transmission, blank=True, null=True)
    mileage = models.BigIntegerField(verbose_name="Пробег", blank=True, null=True)
    drive_unit = models.CharField(verbose_name="Привод", max_length=100, default=None, choices=DriveUnit, blank=True, null=True)
    steering_wheel = models.CharField(verbose_name="Руль", max_length=100, default=None, choices=SteeringWheel, blank=True, null=True)
    pts = models.CharField(verbose_name="Владельцев в ПТС", max_length=10, default=None, choices=Pts, blank=True, null=True)
    year = models.BigIntegerField(verbose_name="Год выпуска", blank=True, null=True)
    price = models.BigIntegerField(verbose_name="Цена", blank=True, null=True)
    state = models.CharField(verbose_name="Состояние автомобиля", max_length=100, default=None, choices=State, blank=True, null=True)
    address = models.CharField(verbose_name='Адрес стоянки', max_length=32, blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class ImageCar(models.Model):
    class Meta:
        db_table = 'car_image'
        verbose_name = 'фото машин'
        verbose_name_plural = 'фотографии машин'
    
    car = models.ForeignKey(Car, verbose_name="Машина", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фотография', upload_to='images/car')
    
    def __str__(self):
        return f'{self.car}'
    
    