# Generated by Django 3.2.8 on 2022-01-17 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_quizdetails_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizdetails',
            name='result',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.PROTECT, to='Quiz.quizresult'),
        ),
    ]
