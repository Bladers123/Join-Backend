# Generated by Django 5.1.2 on 2024-11-23 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(default='Medium', max_length=50),
        ),
    ]
