# Generated by Django 4.1.1 on 2022-10-25 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0009_alter_todo_status_time_alter_todo_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 25, 15, 13, 7, 535544)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='userid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]