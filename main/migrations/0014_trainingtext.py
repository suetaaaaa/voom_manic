# Generated by Django 4.0.6 on 2022-08-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_trainingstudentwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Текст для страницы обучения',
                'verbose_name_plural': 'Текст для страницы обучения',
            },
        ),
    ]
