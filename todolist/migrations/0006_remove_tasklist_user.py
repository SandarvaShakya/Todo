# Generated by Django 3.1.7 on 2021-03-23 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20210317_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='user',
        ),
    ]
