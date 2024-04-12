# Generated by Django 5.0.1 on 2024-01-18 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_variant'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fueltype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_fueltype')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_transmission')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_variant')),
            ],
        ),
    ]
