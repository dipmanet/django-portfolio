# Generated by Django 5.0.3 on 2024-07-25 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0024_alter_testimonial_testimonial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='title',
            new_name='level',
        ),
    ]
