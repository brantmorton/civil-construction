# Generated by Django 2.2.1 on 2019-07-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0003_auto_20190628_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laborer',
            name='completed_application',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='operator',
            name='completed_application',
            field=models.FileField(upload_to=''),
        ),
    ]
