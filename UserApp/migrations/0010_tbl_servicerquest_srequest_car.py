# Generated by Django 5.0.1 on 2024-03-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0009_tbl_servicerquest_scenter_tbl_servicerquest_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_servicerquest',
            name='srequest_car',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
