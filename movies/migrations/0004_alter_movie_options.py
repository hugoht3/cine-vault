# Generated by Django 4.2.16 on 2024-09-27 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_moviecomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-created_on']},
        ),
    ]
