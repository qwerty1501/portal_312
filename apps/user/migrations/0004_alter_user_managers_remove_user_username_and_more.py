# Generated by Django 4.1.4 on 2022-12-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_user_username_alter_user_password"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(
                default="pbkdf2_sha256$390000$zt0esuyMBLYM7yu1hS2tvv$/7OUDEutKjiTg2yTHWx8OOrcRh9LhboT3gC6j8AvCcA=",
                max_length=128,
                verbose_name="Пароль",
            ),
        ),
    ]
