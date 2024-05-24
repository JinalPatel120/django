# Generated by Django 5.0.6 on 2024-05-22 06:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('85550af7-8abb-4472-af3b-fd967129b650'), primary_key=True, serialize=False),
        ),
    ]
