# Generated by Django 5.0.3 on 2024-05-04 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0004_remove_profile_cover_profession_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cover_profession',
        ),
        migrations.AddField(
            model_name='profile',
            name='cover_profession',
            field=models.JSONField(default={}),
        ),
    ]
