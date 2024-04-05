# Generated by Django 5.0 on 2024-04-05 16:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField(verbose_name='Зарплата')),
                ('busyness', models.CharField(max_length=50, verbose_name='Занятость')),
                ('work_schedule', models.CharField(max_length=50, verbose_name='График работы')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название города')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Professions_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=50, verbose_name='Специализация')),
                ('profession', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_application.profession')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='upload/resume', verbose_name='Готовое резюме')),
                ('stage', models.CharField(choices=[('Создание анкеты', 'Создание анкеты'), ('Рассмотрение анкеты', 'Рассмотрение анкеты'), ('Первичное интервью', 'Первичное интервью'), ('3', 'Интервью с заказчиком'), ('4', 'Сбор рекомендаций'), ('5', 'Оффер'), ('6', 'Трудоустройство')], max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profession',
            name='resume',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_application.resume'),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/', verbose_name='Портфолио')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_application.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('native', models.CharField(max_length=50, verbose_name='Родной язык')),
                ('list_languages', models.JSONField(verbose_name='Список языков')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_application.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvl', models.CharField(max_length=50, verbose_name='Уровень')),
                ('lvl_university', models.TextField(verbose_name='Учебное заведение')),
                ('faculty', models.TextField(verbose_name='Факультет')),
                ('specialization', models.TextField(verbose_name='Специализация')),
                ('year_graduatio', models.IntegerField(verbose_name='Год окончания')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_application.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_course', models.TextField(verbose_name='Название курса')),
                ('organization', models.TextField(verbose_name='Проводившая организация')),
                ('specialization', models.TextField(verbose_name='Специализация')),
                ('year_graduation', models.IntegerField(verbose_name='Год окончания')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_application.resume')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Обо мне')),
                ('resume', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_application.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.TextField(verbose_name='Список skills')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_application.resume')),
            ],
        ),
    ]