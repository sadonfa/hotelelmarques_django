# Generated by Django 4.1 on 2022-09-22 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Habitacion', 'verbose_name_plural': 'Habitaciones'},
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.FileField(upload_to='rooms'),
        ),
    ]