# Generated by Django 3.2.8 on 2022-01-03 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resources', '0004_alter_resource_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='chname',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='subcode',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='subname',
        ),
    ]
