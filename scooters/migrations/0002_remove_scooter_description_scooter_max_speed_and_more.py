# Generated by Django 5.1.3 on 2024-11-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scooters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scooter',
            name='description',
        ),
        migrations.AddField(
            model_name='scooter',
            name='max_speed',
            field=models.IntegerField(default=1, verbose_name='Максимальная скорость'),
        ),
        migrations.AddField(
            model_name='scooter',
            name='weight',
            field=models.IntegerField(default=1, verbose_name='Вес'),
        ),
    ]
