from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View

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

@login_required
def create_resume(request):
    if request.method == "POST":
        # form = CreateResumeForm(request.POST)
        # print(form)
        # if form.is_valid():
        user = User.objects.get(pk=request.user.id)
        resume = Resume.objects.create(stage="Создание анкеты", user=user)
        Profession.objects.create(resume=resume, salary=request.POST.get("salary"),
                                  busyness=request.POST.get("busyness"),
                                  work_schedule=request.POST.get("work_schedule"))
        # return HttpResponse("Ошибка")
        # return HttpResponse("Hello")
        return redirect("user_application:create_resume_2")
    else:
        form = CreateResumeForm()
        return render(request, 'user_application/create_resume.html', context={"form": form})


@login_required
def create_resume_2(request):
    if request.method == "POST":
        # form = AddEducationResumeForm(request.POST, request.FILES)
        # if form.is_valid():
        user = User.objects.get(pk=request.user.id)
        resume = Resume.objects.get(user=user, pk=1)
        Education.objects.create(resume=resume, lvl=request.POST.get("lvl_education"),
                                 lvl_university=request.POST.get("lvl_university"), faculty=request.POST.get("faculty"),
                                 specialization=request.POST.get("specialization"),
                                 year_graduatio=request.POST.get("year_graduatio"))
        # return HttpResponse("Hello")
        return redirect("user_application:create_resume_3")
    else:
        form = AddEducationResumeForm()
        return render(request, 'user_application/create_resume.html', context={"form": form})


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
