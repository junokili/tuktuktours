# Generated by Django 3.1.5 on 2021-01-22 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0008_auto_20210122_0331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='name',
            new_name='rating_name',
        ),
        migrations.AddField(
            model_name='rating',
            name='rating_number',
            field=models.IntegerField(default=0),
        ),
    ]
