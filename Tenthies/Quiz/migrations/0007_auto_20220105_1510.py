# Generated by Django 3.2.8 on 2022-01-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_auto_20220105_1504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizresult',
            old_name='answers',
            new_name='correctanswer',
        ),
        migrations.AddField(
            model_name='quizresult',
            name='useranswers',
            field=models.TextField(default=''),
        ),
    ]
