# Generated by Django 3.0.6 on 2020-05-05 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brands',
            new_name='Brand',
        ),
        migrations.RenameModel(
            old_name='OnlineSites',
            new_name='OnlineSite',
        ),
    ]
