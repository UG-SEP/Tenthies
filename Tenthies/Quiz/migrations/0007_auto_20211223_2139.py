# Generated by Django 3.2.8 on 2021-12-23 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_auto_20211222_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='sub_bgcolor_light',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AddField(
            model_name='subject',
            name='sub_boxshadow_color',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AddField(
            model_name='subject',
            name='sub_textcolor_hover',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]