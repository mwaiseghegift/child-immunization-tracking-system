# Generated by Django 4.0.5 on 2022-06-21 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0005_hospital_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hospital',
            options={'ordering': ['name'], 'verbose_name_plural': 'Hospitals'},
        ),
        migrations.AlterModelTable(
            name='county',
            table='counties',
        ),
        migrations.AlterModelTable(
            name='hospital',
            table='hospitals',
        ),
    ]