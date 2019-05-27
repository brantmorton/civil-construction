from django.db import models
from django.contrib.auth.models import User


class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField()
    completed_application = models.FileField()

    def __str__(self):
        return self.name
