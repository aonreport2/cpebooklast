# Generated by Django 3.0.7 on 2021-06-20 02:48

import cropperjs.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0019_auto_20210613_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image_field',
            field=cropperjs.models.CropperImageField(blank=True, null=True, upload_to=''),
        ),
    ]