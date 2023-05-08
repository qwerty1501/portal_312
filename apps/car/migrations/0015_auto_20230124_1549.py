# Generated by Django 3.2.9 on 2023-01-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0014_auto_20230124_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='address',
            field=models.CharField(default=1, max_length=32, verbose_name='Адрес стоянки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='new',
            field=models.BooleanField(default=False, verbose_name='Новый автомобиль'),
        ),
        migrations.AddField(
            model_name='car',
            name='pts',
            field=models.CharField(blank=True, choices=[['1', '1'], ['2', '2'], ['3', '3'], ['+4', '+4']], default=None, max_length=10, null=True, verbose_name='Владельцев в ПТС'),
        ),
    ]