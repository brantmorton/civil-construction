from django.db import models
from django.contrib.auth.models import User


class Laborer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='apply/laborer/resume')
    completed_application = models.FileField(upload_to='apply/laborer/application')

    def __str__(self):
        return self.name


class Operator(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='apply/operator/resume')
    completed_application = models.FileField(upload_to='apply/operator/application')

    def __str__(self):
        return self.name

