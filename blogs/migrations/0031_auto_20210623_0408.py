# Generated by Django 3.0.7 on 2021-06-23 04:08

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0030_userprofile_cropping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='cropping',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_bg_pic',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=0, size=[400, 200], upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=0, size=[300, 300], upload_to=''),
        ),
    ]
