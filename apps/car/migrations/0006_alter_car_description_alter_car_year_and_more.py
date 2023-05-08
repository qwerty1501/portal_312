# Generated by Django 4.1.4 on 2022-12-19 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0005_car_description_car_price_car_year_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="car",
            name="year",
            field=models.BigIntegerField(
                blank=True, null=True, verbose_name="Год выпуска"
            ),
        ),
        migrations.AlterField(
            model_name="imagecar",
            name="image_eight",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/car",
                verbose_name="Фотография 8",
            ),
        ),
        migrations.AlterField(
            model_name="imagecar",
            name="image_five",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/car",
                verbose_name="Фотография 5",
            ),
        ),
        migrations.AlterField(
            model_name="imagecar",
            name="image_four",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/car",
                verbose_name="Фотография 4",
            ),
        ),
        migrations.AlterField(
            model_name="imagecar",
            name="image_one",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/car",
                verbose_name="Фотография 1",
            ),
        ),
        migrations.AlterField(
            model_name="imagecar",
            name="image_seven",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/car",
                verbose_name="Фотография 7",
            ),
        ),
        migrations.AlterField(
            model_name="imagecar",
            name="image_six",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/car",
                verbose_name="Фотография 6",
            ),
        ),
        migrations.AlterField(
            model_name="imagecar",
            name="image_three",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/car",
                verbose_name="Фотография 3",
            ),
        ),
        migrations.AlterField(
            model_name="imagecar",
            name="image_two",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/car",
                verbose_name="Фотография 2",
            ),
        ),
    ]
