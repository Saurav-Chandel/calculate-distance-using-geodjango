# Generated by Django 4.0.3 on 2022-03-17 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_distance_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distance',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='distance',
            name='lon',
        ),
    ]