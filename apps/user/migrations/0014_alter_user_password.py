# Generated by Django 4.1.4 on 2022-12-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0013_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(
                default="pbkdf2_sha256$390000$9t31gDh89KjhDBA91cUxvi$ep7wjf2NM9b4bnNU6Jz/3/mmSRgMdBmMv2I55KCOuQI=",
                max_length=128,
                verbose_name="Пароль",
            ),
        ),
    ]
