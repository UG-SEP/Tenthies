# Generated by Django 3.2.8 on 2022-01-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='', null=True, upload_to='profilePic'),
        ),
    ]
