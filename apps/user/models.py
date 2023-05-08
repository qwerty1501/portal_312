import uuid
import os

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from apps.user.managers import CustomManager
from django.db import models


parametersForNull = {
    'null': True,
    'blank': True,
}


class Rename:
    def __init__(self, path):
        self.path = path;
        
    def rename(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (uuid.uuid4(), ext)
        return os.path.join(self.path, filename)



class User(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи";

    def __str__(self):
        return self.uniqueId.__str__();

    username = None;
    date_joined = None;
    first_name = None;
    last_name = None;
    last_login = None;
    is_active = models.BooleanField(default=True, verbose_name="Активный?");
    is_staff = models.BooleanField(default=False, verbose_name="Админ?");
    is_superuser = models.BooleanField(default=False, verbose_name="СуперАдмин?");
    password = models.CharField(max_length=128, verbose_name="Пароль", default=make_password(settings.DEFAULT_PASSWORD));

    name = models.CharField(max_length=300, verbose_name="Имя", **parametersForNull);
    surname = models.CharField(max_length=300, verbose_name="Фамилия", **parametersForNull);
    company = models.CharField(max_length=300, verbose_name="Компания", **parametersForNull);
    position = models.CharField(max_length=300, verbose_name="Позиция", **parametersForNull);
    workPhone = models.CharField(max_length=300, verbose_name="Рабочий телефон", **parametersForNull);
    personalPhone = models.CharField(max_length=300, verbose_name="Личный телефон", **parametersForNull);
    workEmail = models.EmailField(verbose_name="Рабочий email", **parametersForNull);
    # video = models.ManyToManyField(VideoUser, verbose_name='Видео', blank=True, null=True, related_name='detail_video')
    email = models.EmailField(verbose_name="Личный email", default=None, unique=True, **parametersForNull);
    workWebsite = models.URLField(verbose_name="Рабочий сайт", **parametersForNull);
    otherWebsite = models.URLField(verbose_name="Другой любой сайт", **parametersForNull);
    # fontFamily = models.CharField(max_length=100, default=FONTS[0][0], choices=FONTS, verbose_name="Шрифт", **parametersForNull);

    avatar = models.ImageField(verbose_name="Аватар", upload_to='images/avatars', **parametersForNull);
    avatarHidden = models.BooleanField(default=True)
    # bg = models.ImageField(verbose_name="Задний фон", upload_to=bgRename.rename, **parametersForNull);

    uniqueId = models.UUIDField(unique=True, verbose_name="Уникальный id", **parametersForNull);

    # socials
    whatsapp = models.URLField(verbose_name="Whatsapp", **parametersForNull);
    instagram = models.URLField(verbose_name="Instagram", **parametersForNull);
    facebook = models.URLField(verbose_name="Facebook", **parametersForNull);
    linkedin = models.URLField(verbose_name="Linkedin", **parametersForNull);
    telegram = models.URLField(verbose_name="Telegram", **parametersForNull);
    tiktok = models.URLField(verbose_name="Tiktok", **parametersForNull);
    twitter = models.URLField(verbose_name="Twitter", **parametersForNull);
    youtube = models.URLField(verbose_name="Youtube", **parametersForNull);

    resetPasswordUUID = models.UUIDField(verbose_name="Ссылка для восстановления пароля", **parametersForNull);
    resetPasswordDate = models.BigIntegerField(verbose_name="Время восстановления пароля", **parametersForNull);

    welcome = models.CharField(max_length=200, verbose_name='Строка приветствия', **parametersForNull);
    title = models.CharField(max_length=200, verbose_name="Название", **parametersForNull);
    subtitle = models.CharField(max_length=200, verbose_name="Под заголовок", **parametersForNull);
    description = models.TextField(verbose_name="Описание", **parametersForNull);
    address = models.CharField(max_length=350, verbose_name="Адресс", **parametersForNull);

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomManager()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.uniqueId = uuid.uuid4()
        super(User, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
