from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, FormView

from staff_application.forms import CommentForm
from staff_application.models import HR, Comments
from user_application.models import Resume, Profession, Education, About, Languages, City


class BaseTemplateForStaff(TemplateView):
    template_name = 'user_application/base.html'


class ResumeListView(ListView, LoginRequiredMixin):
    model = Resume
    template_name = "staff_application/resume_list.html"
    context_object_name = 'resume_status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resume = Resume.objects.filter(stage='Создание анкеты', hr=None).select_related('hr')
        context['resume'] = resume
        context["profession"] = Profession.objects.select_related('resume')
        return context


class ResumeStageView(ListView, LoginRequiredMixin):
    model = Resume
    template_name = "staff_application/resume_stage.html"
    context_object_name = 'resume_status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stage = {'nerasobran': 'Создание анкеты', 'phone_interview': 'Телефонное интервью',
                 'interview': 'Собеседование', 'proposal': 'Предложение о работе', 'rejection': 'Отказ'}
        resume = Resume.objects.filter(stage=stage[self.kwargs['stage']],
                                       hr=HR.objects.get(user=self.request.user)).select_related('hr')
        context['resume'] = resume
        context["profession"] = Profession.objects.select_related('resume')
        return context


# Create your views here.
class ResumeUserCheckListView(ListView, LoginRequiredMixin):
    model = Resume
    template_name = "staff_application/resume_user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resume = Resume.objects.get(pk=self.kwargs['pk'])
        context['resume'] = resume
        context["profession"] = Profession.objects.get(resume=resume)
        context["education"] = Education.objects.filter(resume=resume)
        context["about"] = About.objects.get(resume=resume)
        context['languages'] = Languages.objects.filter(resume=resume)
        context['city'] = City.objects.get(resume=resume)
        context['comments'] = Comments.objects.filter(resume=resume)
        hr = HR.objects.get(user=self.request.user)
        resume.hr = hr
        resume.save()

        return context


class AddCommentView(FormView, LoginRequiredMixin):
    form_class = CommentForm
    template_name = "staff_application/comment.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_initial(self):
        initial = super(AddCommentView, self).get_initial()
        if self.request.user.is_authenticated:
            resume = Resume.objects.get(pk=self.kwargs['pk'])
            initial.update(
                {'stage': resume.stage, 'resume': resume, 'hr': resume.hr})
        return initial

    def form_valid(self, form):
        form.save()
        return render(self.request, "staff_application/accept_comment.html")


class RejectionResumeView(TemplateView):
    template_name = 'staff_application/rejection.html'

    def get_context_data(self, **kwargs):
        resume = Resume.objects.get(pk=self.kwargs['pk'])
        resume.stage = 'Отказ'
        resume.save()
        print(self.kwargs['pk'])


class NewStageResumeView(TemplateView):
    template_name = 'staff_application/new_stage.html'

    def get_context_data(self, **kwargs):
        stage_name = ['Создание анкеты', 'Телефонное интервью', 'Собеседование', 'Предложение о работе']
        resume = Resume.objects.get(pk=self.kwargs['pk'])
        if resume.stage == 'Предложение о работе':
            resume.stage = 'Принято'
        else:
            resume.stage = stage_name[stage_name.index(resume.stage) + 1]

        resume.save()
        print(resume)
