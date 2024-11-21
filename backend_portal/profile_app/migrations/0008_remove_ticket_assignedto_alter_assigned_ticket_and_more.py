# Generated by Django 5.1.2 on 2024-11-20 21:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0007_remove_subtask_subtask_id_remove_ticket_subtasks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='assignedTo',
        ),
        migrations.AlterField(
            model_name='assigned',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignedTo', to='profile_app.ticket'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(max_length=50),
        ),
    ]
