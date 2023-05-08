# Generated by Django 4.1.4 on 2022-12-26 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0009_alter_categorycar_options_alter_categorycar_logo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="imagecar",
            old_name="image_one",
            new_name="image",
        ),
        migrations.RemoveField(
            model_name="imagecar",
            name="image_eight",
        ),
        migrations.RemoveField(
            model_name="imagecar",
            name="image_five",
        ),
        migrations.RemoveField(
            model_name="imagecar",
            name="image_four",
        ),
        migrations.RemoveField(
            model_name="imagecar",
            name="image_seven",
        ),
        migrations.RemoveField(
            model_name="imagecar",
            name="image_six",
        ),
        migrations.RemoveField(
            model_name="imagecar",
            name="image_three",
        ),
        migrations.RemoveField(
            model_name="imagecar",
            name="image_two",
        ),
        migrations.AlterField(
            model_name="car",
            name="body_car",
            field=models.CharField(
                blank=True,
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
                default=None,
                max_length=100,
                null=True,
                verbose_name="Тип кузова",
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="drive_unit",
            field=models.CharField(
                blank=True,
                choices=[
                    ["Передний привод", "Передний привод"],
                    ["Задний привод", "Задний привод"],
                    ["Полный привод", "Полный привод"],
                    ["Гибридный привод", "Гибридный привод"],
                ],
                default=None,
                max_length=100,
                null=True,
                verbose_name="Привод",
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="engine",
            field=models.CharField(
                blank=True,
                choices=[
                    ["Бензиновый", "Бензиновый"],
                    ["Дизельный", "Дизельный"],
                    ["Гибридный", "Гибридный"],
                    ["Газ", "Газ"],
                    ["Электрический", "Электрический"],
                ],
                default=None,
                max_length=100,
                null=True,
                verbose_name="Тип двигателя",
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="state",
            field=models.CharField(
                blank=True,
                choices=[
                    ["Отличное", "Отличное"],
                    ["Среднее", "Среднее"],
                    ["Плохое", "Плохое"],
                ],
                default=None,
                max_length=100,
                null=True,
                verbose_name="Состояние автомобиля",
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="steering_wheel",
            field=models.CharField(
                blank=True,
                choices=[["Правый", "Правый"], ["Левый", "Левый"]],
                default=None,
                max_length=100,
                null=True,
                verbose_name="Руль",
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="transmission",
            field=models.CharField(
                blank=True,
                choices=[
                    ["Механическая", "Механическая"],
                    ["Автоматическая", "Автоматическая"],
                    ["Роботизированная", "Роботизированная"],
                    ["Вариативная (бесступенчатая)", "Вариативная (бесступенчатая)"],
                ],
                default=None,
                max_length=100,
                null=True,
                verbose_name="Коробка передач",
            ),
        ),
    ]
