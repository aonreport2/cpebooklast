# Generated by Django 3.0.7 on 2021-06-20 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0021_auto_20210620_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image_field',
        ),
    ]