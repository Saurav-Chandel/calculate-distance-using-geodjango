# Generated by Django 4.0.3 on 2022-03-15 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distance',
            old_name='long',
            new_name='lon',
        ),
    ]