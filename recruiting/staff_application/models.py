from django.db import models
from user_application.models import Resume, HR


# Create your models here.


class Comments(models.Model):
    comment = models.CharField(max_length=250)
    hr = models.ForeignKey(HR, on_delete=models.CASCADE)
    stage = models.CharField(max_length=100)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
