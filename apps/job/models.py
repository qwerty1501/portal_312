from django.db import models

from apps.user.models import User


class CategoryJob(models.Model):
    class Meta:
        db_table = 'categoryjob'
        verbose_name = 'Категория работ'
        verbose_name_plural = 'Категории работ'
        
    name = models.CharField(verbose_name="Категория работ", max_length=100)
    logo = models.ImageField(verbose_name='Фотография', upload_to='images/logo/job', blank=True, null=True)
    
    def __str__(self):
        return self.name


class Job(models.Model):
    class Meta:
        db_table = 'job'
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
    
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    category_job = models.ForeignKey(CategoryJob, verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название работ", max_length=100)
    image = models.ImageField(verbose_name='Фотография', upload_to='images/job', blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    release_date = models.DateField(verbose_name='Дата публикации', auto_now_add=True, blank=True)
    price = models.CharField(verbose_name="Цена", default="Договорная", max_length=100)
    
    def __str__(self):
        return self.name