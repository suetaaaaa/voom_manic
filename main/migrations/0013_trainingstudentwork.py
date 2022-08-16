# Generated by Django 4.0.6 on 2022-08-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_services_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingStudentWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_work_photo', models.ImageField(upload_to='training/student_work_photo/')),
            ],
            options={
                'verbose_name': 'Фото работ учеников',
                'verbose_name_plural': 'Фото работ учеников',
            },
        ),
    ]