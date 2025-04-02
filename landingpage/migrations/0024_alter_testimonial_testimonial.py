# Generated by Django 5.0.3 on 2024-07-16 05:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0023_rename_name_testimonial_submitted_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='list_of_testimonials', to='landingpage.testimonials'),
        ),
    ]
