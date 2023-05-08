# Generated by Django 4.1.4 on 2022-12-19 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0006_alter_car_description_alter_car_year_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="mileage",
            field=models.BigIntegerField(default=1, verbose_name="Пробег"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="car",
            name="volume",
            field=models.BigIntegerField(default=1, verbose_name="Объем двигателя"),
            preserve_default=False,
        ),
    ]
