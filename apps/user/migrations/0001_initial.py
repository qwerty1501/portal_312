# Generated by Django 4.1.4 on 2022-12-20 05:24

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активный?"),
                ),
                ("is_staff", models.BooleanField(default=False, verbose_name="Админ?")),
                (
                    "is_superuser",
                    models.BooleanField(default=False, verbose_name="СуперАдмин?"),
                ),
                (
                    "password",
                    models.CharField(
                        default="pbkdf2_sha256$390000$5vWaq3Qp6Qvvw2ZDf8tXOH$xnXVdb8VK46VwW9iA7XdLMHu9b90RvLkG5VohJHW4xI=",
                        max_length=128,
                        verbose_name="Пароль",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="Имя"
                    ),
                ),
                (
                    "surname",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="Фамилия"
                    ),
                ),
                (
                    "company",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="Компания"
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        blank=True, max_length=300, null=True, verbose_name="Позиция"
                    ),
                ),
                (
                    "workPhone",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="Рабочий телефон",
                    ),
                ),
                (
                    "personalPhone",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="Личный телефон",
                    ),
                ),
                (
                    "workEmail",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="Рабочий email",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        default=None,
                        max_length=254,
                        null=True,
                        unique=True,
                        verbose_name="Личный email",
                    ),
                ),
                (
                    "workWebsite",
                    models.URLField(blank=True, null=True, verbose_name="Рабочий сайт"),
                ),
                (
                    "otherWebsite",
                    models.URLField(
                        blank=True, null=True, verbose_name="Другой любой сайт"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/avatars",
                        verbose_name="Аватар",
                    ),
                ),
                ("avatarHidden", models.BooleanField(default=True)),
                (
                    "uniqueId",
                    models.UUIDField(
                        blank=True, null=True, unique=True, verbose_name="Уникальный id"
                    ),
                ),
                (
                    "whatsapp",
                    models.URLField(blank=True, null=True, verbose_name="Whatsapp"),
                ),
                (
                    "instagram",
                    models.URLField(blank=True, null=True, verbose_name="Instagram"),
                ),
                (
                    "facebook",
                    models.URLField(blank=True, null=True, verbose_name="Facebook"),
                ),
                (
                    "linkedin",
                    models.URLField(blank=True, null=True, verbose_name="Linkedin"),
                ),
                (
                    "telegram",
                    models.URLField(blank=True, null=True, verbose_name="Telegram"),
                ),
                (
                    "snapchat",
                    models.URLField(blank=True, null=True, verbose_name="Snapchat"),
                ),
                (
                    "tiktok",
                    models.URLField(blank=True, null=True, verbose_name="Tiktok"),
                ),
                (
                    "twitter",
                    models.URLField(blank=True, null=True, verbose_name="Twitter"),
                ),
                (
                    "youtube",
                    models.URLField(blank=True, null=True, verbose_name="Youtube"),
                ),
                (
                    "wechat",
                    models.URLField(blank=True, null=True, verbose_name="Wechat"),
                ),
                (
                    "resetPasswordUUID",
                    models.UUIDField(
                        blank=True,
                        null=True,
                        verbose_name="Ссылка для восстановления пароля",
                    ),
                ),
                (
                    "resetPasswordDate",
                    models.BigIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="Время восстановления пароля",
                    ),
                ),
                (
                    "welcome",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Строка приветствия",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Название"
                    ),
                ),
                (
                    "subtitle",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Под заголовок",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=350, null=True, verbose_name="Адресс"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
