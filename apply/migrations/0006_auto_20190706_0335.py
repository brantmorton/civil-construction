# Generated by Django 2.2.1 on 2019-07-06 03:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0005_auto_20190702_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laborer',
            old_name='name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='operator',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='laborer',
            name='lastname',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operator',
            name='lastname',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
