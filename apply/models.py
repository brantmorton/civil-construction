
from django.db import models

"""

    There will be two possible jobs, a Laborer and an Operator.
    Each job application allows for the submission of:
        - last name
        - first name
        - email
        - resume (not required)
        - completed job application
        - date submitted (inherent)
        
"""


class Laborer(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField()
    completed_application = models.FileField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + self.last_name


class Operator(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField()
    completed_application = models.FileField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + self.last_name


