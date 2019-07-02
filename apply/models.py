from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models


class Laborer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='apply/laborer/resume')
    completed_application = models.FileField()

    def __str__(self):
        return self.name


class Operator(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='apply/operator/resume')
    completed_application = models.FileField()

    def __str__(self):
        return self.name

