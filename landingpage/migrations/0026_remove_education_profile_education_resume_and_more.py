# Generated by Django 5.0.3 on 2024-07-25 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0025_rename_title_education_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='profile',
        ),
        migrations.AddField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='landingpage.resume'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='landingpage.resume'),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300, null=True)),
                ('profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='landingpage.profile')),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
    ]
