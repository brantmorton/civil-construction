# Generated by Django 2.2.1 on 2019-07-20 17:15

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20190702_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesBlock1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicesBlock2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', tinymce.models.HTMLField()),
            ],
        ),
    ]
