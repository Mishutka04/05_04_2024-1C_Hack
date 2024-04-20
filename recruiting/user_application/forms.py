import datetime

from django import forms
from django.contrib.auth import get_user_model

from user_application.models import Resume, Profession, Skills, Education, About, Languages, Course


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(disabled=True, label="E-mail", widget=forms.TextInput(attrs={"class": "form-control"}))
    this_year = datetime.date.today().year
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year - 100, this_year - 5))))

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'date_birth', 'email', 'first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Никнейм',
        }  # Метки для полей
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form_input"}),
            'last_name': forms.TextInput(attrs={"class": "form_input"}),
        }


WORK = (("Грузчик", "Грузчик"), ("Программист", "Программист"))
EDUCATION = (("Среднее", "Среднее"), ("Высшее", "Высшее"))
BUSYNESS = (("Полная занятость", "Полная занятость"), ("Частичная ", "Частичная занятость"))
WORK_SCHEDULE = (("Полный ", "Полный день"), ("Удаленная работа", "Удаленная работа"))


class CreateResumeForm(forms.ModelForm):
    file = forms.FileField(required=False)

    class Meta:
        model = Resume
        fields = ['file', 'user']
        widgets = {'user': forms.HiddenInput(), 'file': forms.FileInput(attrs={"class": "form-control", "placeholder": "Готовое резюме"})}


class ProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = '__all__'
        widgets = {'resume': forms.HiddenInput(),
                   'salary': forms.TextInput(attrs={"class": "form-control", "placeholder": "Зарплата"}),
                   'busyness': forms.TextInput(attrs={"class": "form-control", "placeholder": "Занятость"}),
                   'work_schedule': forms.TextInput(attrs={"class": "form-control", "placeholder": "График работы"}), }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        widgets = {'resume': forms.HiddenInput(),
                   'lvl': forms.TextInput(attrs={"class": "form-control", "placeholder": "Уровень образования"}),
                   'lvl_university': forms.TextInput(attrs={"class": "form-control", "placeholder": "Учебное заведение"}),
                   'faculty': forms.TextInput(attrs={"class": "form-control", "placeholder": "Факультет"}),
                   'specialization': forms.TextInput(attrs={"class": "form-control", "placeholder": "Специализация"}),
                   'year_graduatio': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Год окончания"}),}


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        widgets = {'resume': forms.HiddenInput(),
                   'text': forms.Textarea(attrs={"class": "form-control", "placeholder": "Расскажите о себе"}),}


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        widgets = {'resume': forms.HiddenInput(),
                   'skill': forms.Textarea(attrs={"class": "form-control", "placeholder": "Расспишите свои скиллы"})}


class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = '__all__'
        widgets = {'resume': forms.HiddenInput(),
                   'native': forms.TextInput(attrs={"class": "form-control", "placeholder": "Родной язык"}),
                   'list_languages': forms.TextInput(attrs={"class": "form-control", "placeholder": "Иностранные языки"})}


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {'resume': forms.HiddenInput(),
                   'name_course': forms.TextInput(attrs={"class": "form-control", "placeholder": "Название курса"}),
                   'organization': forms.TextInput(attrs={"class": "form-control", "placeholder": "Проводившая организация"}),
                   'specialization': forms.TextInput(attrs={"class": "form-control", "placeholder": "Специализация"}),
                   'year_graduation': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Год окончания"})}
