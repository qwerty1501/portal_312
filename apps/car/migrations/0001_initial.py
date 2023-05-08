# Generated by Django 4.1.4 on 2022-12-17 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CategoryCar",
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
                ("logo", models.CharField(max_length=50, verbose_name="Логотип")),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="Категория машин"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "db_table": "categorycar",
            },
        ),
        migrations.CreateModel(
            name="Car",
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
                (
                    "body_car",
                    models.CharField(
                        choices=[
                            ["Седан", "Седан"],
                            ["Универсал", "Универсал"],
                            ["Хэтчбек", "Хэтчбек"],
                            ["Лифтбек", "Лифтбек"],
                            ["Лимузин", "Лимузин"],
                            ["Внедорожник", "Внедорожник"],
                            ["Кроссовер", "Кроссовер"],
                            ["Стретч", "Стретч"],
                            ["Купе", "Купе"],
                            ["Кабриолет", "Кабриолет"],
                            ["Родстер", "Родстер"],
                            ["Тарга", "Тарга"],
                            ["Пикап", "Пикап"],
                            ["Фургон", "Фургон"],
                            ["Минивэн", "Минивэн"],
                        ],
                        default="Седан",
                        max_length=100,
                        verbose_name="Тип кузова",
                    ),
                ),
                (
                    "engine",
                    models.CharField(
                        choices=[
                            ["Бензиновый", "Бензиновый"],
                            ["Дизельный", "Дизельный"],
                            ["Гибридный", "Гибридный"],
                            ["Газ", "Газ"],
                            ["Электрический", "Электрический"],
                        ],
                        default="Бензиновый",
                        max_length=100,
                        verbose_name="Тип двигателя",
                    ),
                ),
                (
                    "category_car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="car.categorycar",
                        verbose_name="Категория машин",
                    ),
                ),
            ],
            options={
                "verbose_name": "Машина",
                "verbose_name_plural": "Машины",
                "db_table": "car",
            },
        ),
    ]