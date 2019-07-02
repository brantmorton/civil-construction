from django.db import models
from tinymce import models as tinymce_models


class AboutText(models.Model):
    text = tinymce_models.HTMLField()
