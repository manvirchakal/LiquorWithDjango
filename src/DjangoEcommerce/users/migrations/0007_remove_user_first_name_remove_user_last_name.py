# Generated by Django 4.0.1 on 2022-01-24 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
