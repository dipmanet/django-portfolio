# Generated by Django 5.0.3 on 2024-08-16 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0049_profile_profile_picture_alter_portfolio_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='SkillHead',
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name_plural': 'Skills'},
        ),
        migrations.AlterModelOptions(
            name='skillhead',
            options={'verbose_name_plural': 'SkillHeads'},
        ),
    ]
