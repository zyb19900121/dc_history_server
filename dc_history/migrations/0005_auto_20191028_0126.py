# Generated by Django 2.2.6 on 2019-10-28 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dc_history', '0004_auto_20191028_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dynasty',
            name='date_create',
        ),
        migrations.RemoveField(
            model_name='dynasty',
            name='date_update',
        ),
    ]