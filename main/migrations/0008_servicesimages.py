# Generated by Django 4.0.6 on 2022-08-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_mainphoto_alter_certimages_cert_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studio_photo', models.ImageField(upload_to='main/services/')),
                ('training_photo', models.ImageField(upload_to='main/services/')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]