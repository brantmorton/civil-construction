# Generated by Django 2.2.1 on 2019-07-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0004_auto_20190702_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='laborer',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='operator',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
