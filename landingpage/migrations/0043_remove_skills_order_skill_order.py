# Generated by Django 5.0.3 on 2024-08-02 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0042_skills_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='order',
        ),
        migrations.AddField(
            model_name='skill',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
