# Generated by Django 4.0 on 2022-05-31 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_child_birth_county_alter_child_resident_county'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='gender',
            field=models.CharField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default=1, max_length=13),
            preserve_default=False,
        ),
    ]