from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# Расширение модели USER

class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название города")

    def __str__(self):
        return self.name


class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    date_brith = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")
    number_phone = models.IntegerField(verbose_name="Номер телефона", null=True)
    user = models.ForeignKey(City, on_delete=models.CASCADE, null=True)


# Добавить __str__
class Resume(models.Model):
    file = models.FileField(verbose_name='Готовое резюме', upload_to='upload/resume')
    stage = models.Choices() # Сделать
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file

class Comments(models.Model):
    pass
class Profession(models.Model):
    salary = models.IntegerField(verbose_name="Зарплата")
    busyness = models.CharField(max_length=50, verbose_name="Занятость")
    work_schedule = models.CharField(max_length=50, verbose_name="График работы")
    resume = models.OneToOneField(User, on_delete=models.CASCADE)


class Professions_type(models.Model):
    job_name = models.CharField(max_length=50, verbose_name="Тип задания")
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
    lvl_university = models.TextField(verbose_name="Учебное заведение")
    faculty = models.TextField(verbose_name="Факультет")
    specialization = models.TextField(verbose_name="Специализация")
    year_graduatio = models.IntegerField(verbose_name="Год окончания")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Languages(models.Model):
    native = models.CharField(max_length=50, verbose_name="Родной язык")
    list_languages = models.JSONField(verbose_name="Список языков")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Course(models.Model):
    name_course = models.TextField(verbose_name="Название курса")
    organization = models.TextField(verbose_name="Проводившая организация")
    specialization = models.TextField(verbose_name="Специализация")
    year_graduation = models.IntegerField(verbose_name="Год окончания")
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
