from django.db import models

from apps.user.models import User


class CategoryService(models.Model):
    
    class Meta:
        db_table = 'category_service'
        verbose_name = 'Категории сервиса'
        verbose_name_plural = 'Категория сервиса'
        
    name = models.CharField(verbose_name="Название категории", max_length=128)
    
    def __str__(self):
        return self.name
    

class Service(models.Model):
    
    class Meta:
        db_table = 'service'
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
        
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название услуг", max_length=64)
    category = models.ForeignKey(CategoryService, verbose_name="Категория", on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    price = models.BigIntegerField(verbose_name="Цена", blank=True, null=True)
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    
    class Meta:
        db_table = 'comment'
        verbose_name = 'Коментарии'
        verbose_name_plural = 'Коментарии'
        
    service = models.ForeignKey(Service, verbose_name="Услуги", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    title = models.TextField("Коментарии")