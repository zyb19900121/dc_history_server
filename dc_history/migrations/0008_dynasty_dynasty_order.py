# Generated by Django 2.2.6 on 2019-10-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_history', '0007_dynasty_dynasty_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynasty',
            name='dynasty_order',
            field=models.IntegerField(default=1, max_length=11),
        ),
    ]