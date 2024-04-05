import datetime

from django import forms
from django.contrib.auth import get_user_model


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={"class": "form_input"}))
    email = forms.CharField(disabled=True, label="E-mail", widget=forms.TextInput(attrs={"class": "form_input"}))
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


class CreateResumeForm(forms.Form):
    work = forms.ChoiceField(choices=WORK, label='Выберите профессию',
                             widget=forms.Select(attrs={"class": "form_input"}), required=True)
    salary = forms.IntegerField(label='Зарплата',
                                widget=forms.NumberInput(attrs={"class": "form_input"}))
    busyness = forms.ChoiceField(choices=BUSYNESS, label='Занятость',
                                 widget=forms.CheckboxSelectMultiple(attrs={"class": "form_input"}), required=True)
    work_schedule = forms.ChoiceField(choices=WORK_SCHEDULE, label='График работы',
                                      widget=forms.CheckboxSelectMultiple(attrs={"class": "form_input"}), required=True)


class AddEducationResumeForm(forms.Form):
    lvl_education = forms.ChoiceField(choices=EDUCATION, label='Уровень образования',
                                      widget=forms.CheckboxSelectMultiple(attrs={"class": "form_input"}))
    lvl_university = forms.CharField(label='Учебное заведение',
                                     widget=forms.TextInput(attrs={"class": "form_input"}))
    faculty = forms.CharField(label='Факультет',
                              widget=forms.TextInput(attrs={"class": "form_input"}))
    specialization = forms.CharField(label='Специализация',
                                     widget=forms.TextInput(attrs={"class": "form_input"}))
    year_graduatio = forms.IntegerField(max_value=2037, min_value=1950, label='Год окончания',
                                        widget=forms.NumberInput(attrs={"class": "form_input"}))


LANGUAGES = (("Русский", "Русский"), ("Английский", "Английский"))
SKILLS = (("Java", "Java"), ("Python", "Python"))


class AddAboutSkillPortfolioResumeForm(forms.Form):
    about = forms.CharField(label='Уровень образования',
                            widget=forms.TextInput(attrs={"class": "form_input"}))
    skill = forms.MultipleChoiceField(
            choices=SKILLS,
            initial='0',
            widget=forms.SelectMultiple(),
            required=True,
            label='Skill',
        )
    native = forms.ChoiceField(choices=LANGUAGES, label='Родной язык',
                               widget=forms.CheckboxSelectMultiple(attrs={"class": "form_input"}))
    list_languages = forms.ChoiceField(choices=LANGUAGES, label='Иностранный язык',
                                       widget=forms.CheckboxSelectMultiple(attrs={"class": "form_input"}))


class AddCourseResumeForm(forms.Form):
    name_course = forms.CharField(label='Название курса',
                                  widget=forms.TextInput(attrs={"class": "form_input"}))
    organization = forms.CharField(label='Проводившая организация',
                                   widget=forms.TextInput(attrs={"class": "form_input"}))
    specialization = forms.CharField(label='Специализация',
                                     widget=forms.TextInput(attrs={"class": "form_input"}))
    year_graduation = forms.IntegerField(max_value=2037, min_value=1950, label='Год окончания',
                                         widget=forms.NumberInput(attrs={"class": "form_input"}))
