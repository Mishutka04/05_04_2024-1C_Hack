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

CITY = (('Москва', 'Москва'),)


# Добавить __str__
class Resume(models.Model):
    file = models.FileField(verbose_name='Готовое резюме', upload_to='upload/resume', null=True)
    stage = models.CharField(choices=STATE, max_length=50, default='Создание анкеты')  # Сделать
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class City(models.Model):
    name = models.CharField(choices=CITY, max_length=50, verbose_name="Название города")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class HR(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)


class Comments(models.Model):
    pass


class Job(models.Model):
    job = models.CharField(max_length=50, verbose_name="Специализация")

    def __str__(self):
        return self.job


class Profession(models.Model):
    salary = models.IntegerField(verbose_name="Зарплата")
    busyness = models.CharField(max_length=50, verbose_name="Занятость")
    work_schedule = models.CharField(max_length=50, verbose_name="График работы")
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)


SKILLS_CHOICES = (('Python', 'Python'),)


class Skills(models.Model):
    skill = models.CharField(choices=SKILLS_CHOICES, verbose_name="Список skills", max_length=50)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class About(models.Model):
    text = models.TextField(verbose_name="Обо мне")
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE)


class Portfolio(models.Model):
    file = models.FileField(upload_to="uploads/", verbose_name="Портфолио")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


LVL = (('Высшее образование', 'Высшее образование'),)


class Education(models.Model):
    lvl = models.CharField(max_length=50, verbose_name="Уровень", choices=LVL)
    lvl_university = models.CharField(max_length=50, verbose_name="Учебное заведение")
    faculty = models.CharField(max_length=50, verbose_name="Факультет")
    specialization = models.CharField(max_length=50, verbose_name="Специализация")
    year_graduatio = models.IntegerField(verbose_name="Год окончания")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


LANG = (('Русский', 'Русский'),
        ('Английский', 'Английский'),)


class Languages(models.Model):
    native = models.CharField(max_length=50, verbose_name="Родной язык", choices=LANG)
    list_languages = models.CharField(max_length=50, verbose_name="Иностранные языки", choices=LANG, null=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Course(models.Model):
    name_course = models.CharField(max_length=100, verbose_name="Название курса")
    organization = models.CharField(max_length=100, verbose_name="Проводившая организация")
    specialization = models.CharField(max_length=100, verbose_name="Специализация")
    year_graduation = models.IntegerField(verbose_name="Год окончания")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

# Create your models here.
