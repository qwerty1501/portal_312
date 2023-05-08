# Generated by Django 4.1.4 on 2023-01-07 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RealEstate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="Название")),
                ("address", models.IntegerField(verbose_name="Адрес")),
                (
                    "flat",
                    models.IntegerField(blank=True, null=True, verbose_name="Квартира"),
                ),
                (
                    "entrance",
                    models.IntegerField(blank=True, null=True, verbose_name="Пподъезд"),
                ),
                (
                    "floor",
                    models.IntegerField(blank=True, null=True, verbose_name="Этаж"),
                ),
                (
                    "house",
                    models.IntegerField(blank=True, null=True, verbose_name="Дом"),
                ),
                (
                    "price",
                    models.BigIntegerField(blank=True, null=True, verbose_name="Цена"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Недвижимость",
                "verbose_name_plural": "Недвижимость",
                "db_table": "real_estate",
            },
        ),
    ]