# Generated by Django 2.2.1 on 2019-07-02 20:03

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abouttext',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]