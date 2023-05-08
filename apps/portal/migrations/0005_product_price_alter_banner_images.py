# Generated by Django 4.1.4 on 2022-12-26 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0004_banner"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.BigIntegerField(default=1, verbose_name="Цена"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="banner",
            name="images",
            field=models.ImageField(
                upload_to="images/bannre", verbose_name="Фотография"
            ),
        ),
    ]