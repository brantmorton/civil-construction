# Generated by Django 2.2.1 on 2019-07-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0007_auto_20190706_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laborer',
            name='resume',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='operator',
            name='resume',
            field=models.FileField(upload_to=''),
        ),
    ]
