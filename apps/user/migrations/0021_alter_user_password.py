# Generated by Django 3.2.9 on 2023-01-23 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$wo6BuNUkf3ylgy0o8Kcibw$LMscRM1N4ntCe7AQY9exUBhcs+OHKEPyxlBQcEjpnFU=', max_length=128, verbose_name='Пароль'),
        ),
    ]