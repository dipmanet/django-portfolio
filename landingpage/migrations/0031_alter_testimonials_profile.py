# Generated by Django 5.0.3 on 2024-07-26 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0030_alter_testimonials_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='profile',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='landingpage.profile'),
        ),
    ]
