# Generated by Django 3.2.8 on 2021-12-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0005_subject_totalquestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='sub_bgcolor',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AddField(
            model_name='subject',
            name='subimg',
            field=models.ImageField(default='', upload_to='E:\\HTML,CSS,Javascript\\Django\\Django Learning\\Tenthies\\static/images'),
        ),
    ]
