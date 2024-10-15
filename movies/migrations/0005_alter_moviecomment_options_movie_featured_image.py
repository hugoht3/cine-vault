# Generated by Django 4.2.16 on 2024-10-15 13:16

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moviecomment',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='movie',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
