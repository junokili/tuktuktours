# Generated by Django 3.1.5 on 2021-01-20 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_blogpost_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blogpost',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blogs.blogpost'),
        ),
    ]
