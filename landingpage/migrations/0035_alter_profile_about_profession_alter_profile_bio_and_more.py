# Generated by Django 5.0.3 on 2024-07-30 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0034_alter_websiteprofile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_profession',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cover_profession',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='degree',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
