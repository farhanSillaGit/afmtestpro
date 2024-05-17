# Generated by Django 5.0.6 on 2024-05-16 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_chunk'),
    ]

    operations = [
        migrations.AddField(
            model_name='chunk',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='chunk',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='chunk',
            name='file_path',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='chunk',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
