from django.db import models
from tinymce import models as tinymce_models


class AboutText(models.Model):
    text = tinymce_models.HTMLField()


class ServicesBlock1(models.Model):
    text = tinymce_models.HTMLField()


class ServicesBlock2(models.Model):
    text = tinymce_models.HTMLField()