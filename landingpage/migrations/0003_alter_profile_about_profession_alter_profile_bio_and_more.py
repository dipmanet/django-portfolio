# Generated by Django 5.0.3 on 2024-04-20 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0002_stringvalue_remove_profile_contact_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_profession',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='cover_profession',
        ),
        migrations.AddField(
            model_name='profile',
            name='cover_profession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landingpage.stringvalue'),
        ),
    ]
