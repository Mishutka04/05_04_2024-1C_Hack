import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm

from authentication.models import Code


class LoginUserForm(AuthenticationForm):
    # username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        field = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={"class": "form_input"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form_input"}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={"class": "form_input"}))
    code = forms.CharField(label='Индивидуальный код', widget=forms.TextInput(attrs={"class": "form_input"}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Никнейм',
        }  # Метки для полей
        widgets = {
            'email': forms.TextInput(attrs={"class": "form_input"}),
            'first_name': forms.TextInput(attrs={"class": "form_input"}),
            'last_name': forms.TextInput(attrs={"class": "form_input"}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password1']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email

    def clean_code(self):
        code = self.cleaned_data['code']
        if Code.objects.get(code=code):
            return code
        raise forms.ValidationError("Неправильный код доступа!")


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


class ProfilePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={"class": "form_input"}))
    new_password1 = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={"class": "form_input"}))
    new_password2 = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={"class": "form_input"}))


class CodeGeneratorForm(forms.Form):
    email = forms.CharField(label="E-mail", widget=forms.TextInput(attrs={"class": "form_input"}))
