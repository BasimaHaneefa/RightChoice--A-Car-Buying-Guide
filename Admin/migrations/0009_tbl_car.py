# Generated by Django 5.0.1 on 2024-01-18 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_delete_tbl_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_year', models.CharField(max_length=20)),
                ('car_mileage', models.CharField(max_length=30)),
                ('car_price', models.CharField(max_length=50)),
                ('engine_size', models.CharField(max_length=30)),
                ('car_horsepower', models.CharField(max_length=30)),
                ('car_torque', models.CharField(max_length=30)),
                ('car_photo', models.FileField(upload_to='Car/')),
                ('seat_capacity', models.CharField(max_length=30)),
                ('car_gear', models.CharField(max_length=30)),
                ('car_tire', models.CharField(max_length=30)),
                ('bodytype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_bodytype')),
                ('fueltype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_fueltype')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_transmission')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_variant')),
            ],
        ),
    ]
