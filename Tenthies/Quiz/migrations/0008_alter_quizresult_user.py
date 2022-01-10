# Generated by Django 3.2.8 on 2022-01-06 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_muser'),
        ('Quiz', '0007_auto_20220105_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizresult',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='User.muser'),
        ),
    ]
