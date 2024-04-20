from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.models import User

STATE = (("Создание анкеты", "Создание анкеты"),
         ("Рассмотрение анкеты", "Рассмотрение анкеты"),
         ("Первичное интервью", "Первичное интервью"),
         ("3", "Интервью с заказчиком"),
         ("4", "Сбор рекомендаций"),
         ("5", "Оффер"),
         ("6", "Трудоустройство"),)


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название города")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


# Добавить __str__
class Resume(models.Model):
    file = models.FileField(verbose_name='Готовое резюме', upload_to='upload/resume', null=True)
    stage = models.CharField(choices=STATE, max_length=50, default='Создание анкеты')  # Сделать
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.stage


class Comments(models.Model):
    pass


class Profession(models.Model):
    salary = models.IntegerField(verbose_name="Зарплата")
    busyness = models.CharField(max_length=50, verbose_name="Занятость")
    work_schedule = models.CharField(max_length=50, verbose_name="График работы")
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)


class Professions_type(models.Model):
    job_name = models.CharField(max_length=50, verbose_name="Специализация")
    profession = models.OneToOneField(Profession, on_delete=models.CASCADE)


class Skills(models.Model):
    skill = models.TextField(verbose_name="Список skills")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class About(models.Model):
    text = models.TextField(verbose_name="Обо мне")
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)


class Portfolio(models.Model):
    file = models.FileField(upload_to="uploads/", verbose_name="Портфолио")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Education(models.Model):
    lvl = models.CharField(max_length=50, verbose_name="Уровень")
    lvl_university = models.CharField(max_length=50, verbose_name="Учебное заведение")
    faculty = models.CharField(max_length=50, verbose_name="Факультет")
    specialization = models.CharField(max_length=50, verbose_name="Специализация")
    year_graduatio = models.IntegerField(verbose_name="Год окончания")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Languages(models.Model):
    native = models.CharField(max_length=50, verbose_name="Родной язык")
    list_languages = models.CharField(max_length=50, verbose_name="Иностранные языки")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Course(models.Model):
    name_course = models.CharField(max_length=100,verbose_name="Название курса")
    organization = models.CharField(max_length=100,verbose_name="Проводившая организация")
    specialization = models.CharField(max_length=100,verbose_name="Специализация")
    year_graduation = models.IntegerField(verbose_name="Год окончания")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

# Create your models here.
