# Generated by Django 3.1.5 on 2021-01-19 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20210119_0827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog',
            new_name='post',
        ),
    ]