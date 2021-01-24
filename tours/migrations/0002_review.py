# Generated by Django 3.1.5 on 2021-01-20 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=254)),
                ('author', models.CharField(default='', max_length=50)),
                ('review_content', models.TextField()),
                ('review_rating', models.IntegerField(default=0)),
                ('writtenon', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tours.tour')),
            ],
            options={
                'ordering': ['writtenon'],
            },
        ),
    ]