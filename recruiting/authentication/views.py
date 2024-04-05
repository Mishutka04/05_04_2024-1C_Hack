from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, PasswordChangeView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
import uuid
from authentication.forms import LoginUserForm, RegisterUserForm, ProfileEditForm, ProfilePasswordChangeForm


# Create your views here.

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "authentication/login.html"

    def get_success_url(self):
        return reverse_lazy('user_application:create_resume')


# def login_user(request):
#    if request.method == "POST":
#        form = LoginUserForm(request.POST)
#        if form.is_valid():
#            cd = form.cleaned_data
#            user = authenticate(request, username=cd['username'], password=cd['password'])
#            if user and user.is_active:
#                login(request, user)
#                return HttpResponseRedirect(reverse('subject'))
#    else:
#        form = LoginUserForm()
#    return render(request, 'authentication/login.html', context={'form': form})
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('profile:login')


class ProfileEdit(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileEditForm
    login_url = '/login/'
    template_name = 'authentication/profile_edit.html'

    def get_success_url(self):  # Перенаправление
        return reverse_lazy('profile:edit')

    def get_object(self, queryset=None):
        return self.request.user


class ShowProfile(LoginRequiredMixin, DetailView):
    model = get_user_model()
    login_url = '/login/'
    template_name = 'authentication/profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class ProfilePasswordChange(PasswordChangeView):
    form_class = ProfilePasswordChangeForm
    success_url = reverse_lazy("profile:password_change_done")
    template_name = 'authentication/password_change_form.html'

    # def get_object(self, queryset=None):
    #    return get_object_or_404(Класс user, )


def create_resume(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'authentication/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'authentication/register.html', context={"form": form})


#

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('subject'))
