# Generated by Django 5.0.3 on 2024-07-15 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0016_alter_experience_company_alter_experience_date_to'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='title',
            new_name='position',
        ),
    ]
