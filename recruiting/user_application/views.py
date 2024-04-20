from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView, ListView
from user_application.forms import *
from user_application.models import Resume, Profession, About, Languages, Education


class CreateResume(FormView, LoginRequiredMixin):
    form_class = CreateResumeForm
    template_name = "user_application/create_resume.html"

    def get_initial(self):
        initial = super(CreateResume, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'user': self.request.user})
        return initial

    def form_valid(self, form):
        Event = form.save()
        return redirect("user_application:select_city", pk=Event.pk)


class CityView(FormView, LoginRequiredMixin):
    form_class = CityForm
    template_name = "user_application/create_resume.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['title'] = "Выберите город"
        return context

    def get_initial(self):
        initial = super(CityView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'resume': Resume.objects.get(user=self.request.user, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):
        Event = form.save()
        return redirect("user_application:create_profession", pk=self.kwargs['pk'])


class ProfessionView(FormView, LoginRequiredMixin):
    form_class = ProfessionForm
    template_name = "user_application/create_resume.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['title'] = "Выберите профессию"
        return context

    def get_initial(self):
        initial = super(ProfessionView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'resume': Resume.objects.get(user=self.request.user, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):
        form.save()
        return redirect("user_application:create_education", pk=self.kwargs['pk'])


class EducationView(FormView, LoginRequiredMixin):
    form_class = EducationForm
    template_name = "user_application/create_resume.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['title'] = "Выберите уровень образования"
        return context

    def get_initial(self):
        initial = super(EducationView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'resume': Resume.objects.get(user=self.request.user, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):
        Event = form.save()
        return redirect("user_application:create_about", pk=self.kwargs['pk'])


class AboutView(FormView, LoginRequiredMixin):
    form_class = AboutForm
    template_name = "user_application/create_resume.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_initial(self):
        initial = super(AboutView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'resume': Resume.objects.get(user=self.request.user, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):
        form.save()
        return redirect("user_application:create_skills", pk=self.kwargs['pk'])


class SkillsView(FormView, LoginRequiredMixin):
    form_class = SkillsForm
    template_name = "user_application/create_resume.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['title'] = "Выберите Skill"
        return context

    def get_initial(self):
        initial = super(SkillsView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'resume': Resume.objects.get(user=self.request.user, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):
        form.save()
        return redirect("user_application:create_languages", pk=self.kwargs['pk'])


class LanguagesView(FormView, LoginRequiredMixin):
    form_class = LanguagesForm
    template_name = "user_application/create_resume.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['title'] = "Выберите язык"
        return context

    def get_initial(self):
        initial = super(LanguagesView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'resume': Resume.objects.get(user=self.request.user, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):
        form.save()
        return redirect("user_application:create_course", pk=self.kwargs['pk'])


class CourseView(FormView, LoginRequiredMixin):
    form_class = CourseForm
    template_name = "user_application/create_resume.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_initial(self):
        initial = super(CourseView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'resume': Resume.objects.get(user=self.request.user, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):
        Event = form.save()
        return redirect("user_application:resume_list")


class ResumeListView(ListView, LoginRequiredMixin):
    model = Resume
    template_name = "user_application/resume_list.html"
    context_object_name = 'resume_status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['resume'] = Resume.objects.filter(user=self.request.user)
        context["profession"] = Profession.objects.filter(resume__user=self.request.user)
        return context


class ResumeCheckListView(ListView, LoginRequiredMixin):
    model = Resume
    template_name = "user_application/resume.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resume = Resume.objects.get(user=self.request.user, pk=self.kwargs['pk'])
        context['resume'] = resume
        context["profession"] = Profession.objects.get(resume=resume)
        context["education"] = Education.objects.filter(resume=resume)
        context["about"] = About.objects.get(resume=resume)
        context['languages'] = Languages.objects.filter(resume=resume)
        context['city'] = City.objects.get(resume=resume)

        return context
