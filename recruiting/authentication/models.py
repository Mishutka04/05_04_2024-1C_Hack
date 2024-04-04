from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# Расширение модели USER
class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    date_brith = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")
    city = models.CharField(max_length=50, verbose_name="Тип задания")
    number_phone = models.IntegerField(max_length=11, verbose_name="Номер телефона")


class Profession(models.Model):
    pass


class Skills(models.Model):
    pass


class About(models.Model):
    pass


class Portfolio(models.Model):
    pass


class Education(models.Model):
    pass


class Languages(models.Model):
    pass


class Course(models.Model):
    pass
