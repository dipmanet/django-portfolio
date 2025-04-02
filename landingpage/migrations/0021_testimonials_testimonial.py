# Generated by Django 5.0.3 on 2024-07-16 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0020_alter_service_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300, null=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='landingpage.profile')),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200, null=True)),
                ('Testimonial', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='list_of_Testimonials', to='landingpage.testimonials')),
            ],
        ),
    ]
