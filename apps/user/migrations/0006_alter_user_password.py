# Generated by Django 4.1.4 on 2022-12-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_remove_user_snapchat_remove_user_wechat_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(
                default="pbkdf2_sha256$390000$Yx6s5FbQdu2LiWWP5zKxAR$s8uRzbviEHaHR9fZAydScAYQEzb5bnPzDV21VmfbosY=",
                max_length=128,
                verbose_name="Пароль",
            ),
        ),
    ]
