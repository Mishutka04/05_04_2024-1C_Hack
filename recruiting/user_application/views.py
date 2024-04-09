from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView

from authentication.models import User
from user_application.forms import *
from user_application.models import Resume, Profession, Course, About, Skills, Portfolio, Languages, Education


# Create your views here.
# class MyCreateView(View):
#    template_name = 'form.html'
#    form_class = MyForm
#
#    def get(self, request, *args, **kwargs):
#        form = self.form_class
#        return render(request, template_name, {'form': form})
#
#    def post(self, request, *args, **kwargs):
#        form = self.form_class(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResonseRedirect(reverse('list-view'))
#        else:
#            return render(request, self.template_name, {'form': form})
class CreateResume(FormView):
    form_class = CreateResumeForm
    template_name = "user_application/create_resume.html"

    def get_initial(self):
        initial = super(CreateResume, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'user': self.request.user})
        return initial

    def form_valid(self, form):
        Event = form.save()
        print(Event.pk)
        return redirect("user_application:create_profession", pk=Event.pk)
        ## extra_context = {}


class ProfessionView(FormView):
    form_class = ProfessionForm
    template_name = "user_application/create_resume.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_initial(self):
        initial = super(ProfessionView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'resume': Resume.objects.get(user=self.request.user, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):
        form.save()
        return redirect("user_application:create_education", pk=self.kwargs['pk'])


class EducationView(FormView):
    form_class = EducationForm
    template_name = "user_application/create_resume.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_initial(self):
        initial = super(EducationView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'resume': Resume.objects.get(user=self.request.user, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):
        Event = form.save()
        return redirect("user_application:create_about", pk=self.kwargs['pk'])


class AboutView(FormView):
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


class SkillsView(FormView):
    form_class = SkillsForm
    template_name = "user_application/create_resume.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_initial(self):
        initial = super(SkillsView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'resume': Resume.objects.get(user=self.request.user, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):
        form.save()
        return redirect("user_application:create_languages", pk=self.kwargs['pk'])


class LanguagesView(FormView):
    form_class = LanguagesForm
    template_name = "user_application/create_resume.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_initial(self):
        initial = super(LanguagesView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'resume': Resume.objects.get(user=self.request.user, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):
        form.save()
        return redirect("user_application:create_course", pk=self.kwargs['pk'])


class CourseView(FormView):
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
        return redirect("user_application:create_resume_2", pk=Event.pk)


# @login_required
# def create_resume1(request):
#    if request.method == 'POST':
#
#        company_form = CreateResumeForm(request.POST)
#        account_form = ProfessionForm(request.POST)
#
#        if company_form.is_valid() and account_form.is_valid():
#
#            company_form.user = request.user
#            company_form.save()
#            # account_form.save()
#            return HttpResponse('/success')
#
#        else:
#            context = {'context': [
#                company_form,
#                account_form,
#            ]}
#
#    else:
#        initial = {'user': request.user}
#        context = {"context": [
#            CreateResumeForm(initial=initial),
#            ProfessionForm(),
#        ]}
#
#    return render(request, 'user_application/create_resume.html', context)


# @login_required
# def create_resume(request):
#    if request.method == "POST":
#        # form = CreateResumeForm(request.POST)
#        # print(form)
#        # if form.is_valid():
#        user = User.objects.get(pk=request.user.id)
#        resume = Resume.objects.create(stage="Создание анкеты", user=user)
#        Profession.objects.create(resume=resume, salary=request.POST.get("salary"),
#                                  busyness=request.POST.get("busyness"),
#                                  work_schedule=request.POST.get("work_schedule"))
#        # return HttpResponse("Ошибка")
#        # return HttpResponse("Hello")
#        return redirect("user_application:create_resume_2")
#    else:
#        form = CreateResumeForm()
#        return render(request, 'user_application/create_resume.html', context={"form": form})


# @login_required
# def create_resume_2(request):
#    if request.method == "POST":
#        # form = AddEducationResumeForm(request.POST, request.FILES)
#        # if form.is_valid():
#        user = User.objects.get(pk=request.user.id)
#        resume = Resume.objects.get(user=user, pk=1)
#        Education.objects.create(resume=resume, lvl=request.POST.get("lvl_education"),
#                                 lvl_university=request.POST.get("lvl_university"), faculty=request.POST.get("faculty"),
#                                 specialization=request.POST.get("specialization"),
#                                 year_graduatio=request.POST.get("year_graduatio"))
#        # return HttpResponse("Hello")
#        return redirect("user_application:create_resume_3")
#    else:
#        form = AddEducationResumeForm()
#        return render(request, 'user_application/create_resume.html', context={"form": form})
#

@login_required
def create_resume_3(request):
    if request.method == "POST":
        # form = AddAboutSkillPortfolioResumeForm(request.POST, request.FILES)
        # if form.is_valid():
        user = User.objects.get(pk=request.user.id)
        resume = Resume.objects.get(user=user, pk=3)
        About.objects.create(resume=resume, text=request.POST.get("about"))
        Skills.objects.create(resume=resume, skill=request.POST.get("skill"))
        # Portfolio.objects.create(resume=resume, file=form.cleaned_data['file'])
        Languages.objects.create(resume=resume, native=request.POST.get("native"),
                                 list_languages=request.POST.get("list_languages"))
        # return HttpResponse("Hello")
        return redirect("user_application:create_resume_4")
    else:
        form = AddAboutSkillPortfolioResumeForm()
        return render(request, 'user_application/create_resume.html', context={"form": form})


@login_required
def create_resume_4(request):
    if request.method == "POST":
        # form = AddCourseResumeForm(request.POST, request.FILES)
        # if form.is_valid():
        user = User.objects.get(pk=request.user.id)
        resume = Resume.objects.get(user=user, pk=1)
        Course.objects.create(resume=resume, name_course=request.POST.get("name_course"),
                              organization=request.POST.get("organization"),
                              specialization=request.POST.get("specialization"),
                              year_graduation=request.POST.get("year_graduation"))
        # return HttpResponse("Hello")
        return HttpResponse("Все окончено!")
    else:
        form = AddCourseResumeForm()
        return render(request, 'user_application/create_resume.html', context={"form": form})
