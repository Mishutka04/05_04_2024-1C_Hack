from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from user_application.models import Resume, Profession, HR


class BaseTemplateForStaff(TemplateView):
    template_name = 'staff_application/base_for_staff.html'


class ResumeListView(ListView):
    model = Resume
    template_name = "staff_application/resume_list.html"
    context_object_name = 'resume_status'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume'] = Resume.objects.filter(hr__user=self.request.user)
        print(Resume.objects.filter(hr__user=self.request.user))
        context["profession"] = Profession.objects.filter(resume=Resume.pk)
        return context
# Create your views here.
