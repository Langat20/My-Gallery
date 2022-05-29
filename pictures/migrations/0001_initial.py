# Generated by Django 4.0.4 on 2022-05-28 17:50

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Galore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('image', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image/')),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='pictures.category')),
                ('location', models.ManyToManyField(to='pictures.location')),
            ],
        ),
    ]
