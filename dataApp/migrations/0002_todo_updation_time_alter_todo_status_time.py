# Generated by Django 4.1.1 on 2022-10-25 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='updation_time',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 25, 13, 48, 58, 574691)),
        ),
    ]
