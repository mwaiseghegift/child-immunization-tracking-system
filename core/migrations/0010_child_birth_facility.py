# Generated by Django 4.0 on 2022-06-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_childimmunization_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='birth_facility',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
