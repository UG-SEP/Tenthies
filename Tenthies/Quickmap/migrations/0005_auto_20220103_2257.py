# Generated by Django 3.2.8 on 2022-01-03 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quickmap', '0004_alter_quickmap_quickmap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quickmap',
            name='chname',
        ),
        migrations.RemoveField(
            model_name='quickmap',
            name='subcode',
        ),
        migrations.RemoveField(
            model_name='quickmap',
            name='subname',
        ),
    ]