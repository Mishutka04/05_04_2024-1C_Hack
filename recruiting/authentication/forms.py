import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class BootstrapTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['class'] = 'form-control'


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        field = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}),
            'password': forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}),

        }
        labels = {
            'username': 'Логин',
            'password': 'Пароль',
        }

    username.widget.attrs.update(id="email")


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Логин"}))
    password1 = forms.CharField(label="Пароль",
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Пароль"}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Повтор пароля"}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Никнейм',
        }  # Метки для полей
        widgets = {
            'email': forms.TextInput(attrs={"class": "form-control", "placeholder": "Почта"}),
            'first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Фамилия"}),
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


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Никнейм',
        }  # Метки для полей
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Начальное имя"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Псевдоним"}),
        }


class ProfilePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={"class": "form_input"}))
    new_password1 = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={"class": "form_input"}))
    new_password2 = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={"class": "form_input"}))
