# Generated by Django 4.0.4 on 2022-05-31 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='room_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='device',
            name='serial_number',
            field=models.PositiveIntegerField(),
        ),
    ]
