# Generated by Django 3.0.7 on 2020-06-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_cpeaccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpeaccount',
            name='cpenumber',
            field=models.CharField(max_length=20),
        ),
    ]