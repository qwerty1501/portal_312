# Generated by Django 3.2.9 on 2023-01-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='bannerfour',
            name='name',
            field=models.CharField(default=1, max_length=64, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bannerone',
            name='name',
            field=models.CharField(default=1, max_length=64, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bannerthree',
            name='name',
            field=models.CharField(default=1, max_length=64, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bannertwo',
            name='name',
            field=models.CharField(default=1, max_length=64, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Одобренный'),
        ),
    ]