# Generated by Django 4.1.4 on 2022-12-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0005_product_price_alter_banner_images"),
    ]

    operations = [
        migrations.CreateModel(
            name="BannerOne",
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
                    "images",
                    models.ImageField(
                        upload_to="images/bannre", verbose_name="Фотография"
                    ),
                ),
                ("url", models.URLField(verbose_name="Укажите url ссылку")),
            ],
            options={
                "verbose_name": "Баннер",
                "verbose_name_plural": "Баннеры",
                "db_table": "banner_one",
            },
        ),
        migrations.CreateModel(
            name="BannerThree",
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
                    "images",
                    models.ImageField(
                        upload_to="images/bannre", verbose_name="Фотография"
                    ),
                ),
                ("url", models.URLField(verbose_name="Укажите url ссылку")),
            ],
            options={
                "verbose_name": "Баннер",
                "verbose_name_plural": "Баннеры",
                "db_table": "banner_three",
            },
        ),
        migrations.CreateModel(
            name="BannerTwo",
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
                    "images",
                    models.ImageField(
                        upload_to="images/bannre", verbose_name="Фотография"
                    ),
                ),
                ("url", models.URLField(verbose_name="Укажите url ссылку")),
            ],
            options={
                "verbose_name": "Баннер",
                "verbose_name_plural": "Баннеры",
                "db_table": "banner_two",
            },
        ),
        migrations.RenameModel(
            old_name="Banner",
            new_name="BannerFour",
        ),
        migrations.AlterModelTable(
            name="bannerfour",
            table="banner_four",
        ),
    ]