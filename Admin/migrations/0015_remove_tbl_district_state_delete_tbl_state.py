# Generated by Django 4.2.7 on 2024-03-07 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0014_tbl_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_district',
            name='state',
        ),
        migrations.DeleteModel(
            name='tbl_state',
        ),
    ]
