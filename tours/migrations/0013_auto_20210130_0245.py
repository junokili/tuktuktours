# Generated by Django 3.1.5 on 2021-01-30 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0012_tour_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(default='', max_length=254),
        ),
    ]
