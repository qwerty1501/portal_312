# Generated by Django 4.1.4 on 2022-12-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0002_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="logo",
            field=models.ImageField(
                default=1, upload_to="images/logo/prod", verbose_name="Фотография"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="name",
            field=models.CharField(default=1, max_length=128, verbose_name=""),
            preserve_default=False,
        ),
    ]
