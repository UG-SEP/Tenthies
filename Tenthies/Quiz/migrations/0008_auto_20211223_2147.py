# Generated by Django 3.2.8 on 2021-12-23 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0007_auto_20211223_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='sub_bgcolor_light',
            field=models.CharField(default='#000000', max_length=10),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_boxshadow_color',
            field=models.CharField(default='#000000', max_length=10),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_textcolor_hover',
            field=models.CharField(default='#000000', max_length=10),
        ),
    ]
