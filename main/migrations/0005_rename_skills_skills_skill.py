# Generated by Django 4.0.6 on 2022-08-14 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_skills_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='skills',
            new_name='skill',
        ),
    ]