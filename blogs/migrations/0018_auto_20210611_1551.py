# Generated by Django 3.0.7 on 2021-06-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_userotp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='count',
            field=models.BooleanField(verbose_name=False),
        ),
    ]
