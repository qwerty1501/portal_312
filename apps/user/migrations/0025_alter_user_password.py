# Generated by Django 3.2.9 on 2023-01-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$1uJ5995d7Pk9yKxbbOWfuG$jS2m/xGneFFUUEdiY0pxHP8QTKoNEL2uedCfU5/ancY=', max_length=128, verbose_name='Пароль'),
        ),
    ]
