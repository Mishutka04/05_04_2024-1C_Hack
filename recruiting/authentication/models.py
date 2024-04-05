from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    date_brith = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")
    number_phone = models.IntegerField(verbose_name="Номер телефона", null=True)
