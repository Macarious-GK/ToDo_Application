# Generated by Django 4.2.6 on 2023-10-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tooodooo', '0002_alter_tasks_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
