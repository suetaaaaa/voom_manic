# Generated by Django 4.0.6 on 2022-08-11 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voomuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
