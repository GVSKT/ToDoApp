# Generated by Django 4.1.1 on 2022-10-25 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0003_remove_todo_id_todo_userid_alter_todo_status_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 25, 14, 53, 16, 778053)),
        ),
    ]
