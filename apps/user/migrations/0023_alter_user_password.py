# Generated by Django 3.2.9 on 2023-01-24 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$BllTKtzCOvWojCaKWkVzYf$f2i2R/q1DSBTx+fimBkRx1A/HFVkS7gE9DbvX+vn6Ww=', max_length=128, verbose_name='Пароль'),
        ),
    ]