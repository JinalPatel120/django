# Generated by Django 5.0.6 on 2024-05-27 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_app', '0004_alter_info_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='email',
        ),
        migrations.AddField(
            model_name='info',
            name='city',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
