from django.contrib import admin

from user_application.models import Resume, Profession, Job, About

admin.site.register(Resume)
admin.site.register(Profession)
admin.site.register(Job)
admin.site.register(About)
# Register your models here.
