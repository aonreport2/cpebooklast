# Generated by Django 3.0.7 on 2021-05-13 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_auto_20210512_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]