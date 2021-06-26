# Generated by Django 3.0.7 on 2021-06-23 03:22

import cropperjs.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0026_auto_20210623_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=cropperjs.models.CropperImageField(aspectratio='1.0', dimensions=(300, 300), upload_to='images'),
        ),
    ]
