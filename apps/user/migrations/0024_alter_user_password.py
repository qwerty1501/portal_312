# Generated by Django 3.2.9 on 2023-01-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$Eg8ImAcyQNvcZcZTCLJI3T$8PsF6t0d4ONQYAKCL6dAjFBBCkpbMsIIFwKkSFaFsDU=', max_length=128, verbose_name='Пароль'),
        ),
    ]