from django.db import models
from tinymce import models as tinymce_models

"""

Each of these utilize tinymce's HTMLField model to 
allow dynamic HTML content updating from the admin page

"""


class AboutText(models.Model):
    text = tinymce_models.HTMLField()


class ServicesBlock1(models.Model):
    text = tinymce_models.HTMLField()


class ServicesBlock2(models.Model):
    text = tinymce_models.HTMLField()