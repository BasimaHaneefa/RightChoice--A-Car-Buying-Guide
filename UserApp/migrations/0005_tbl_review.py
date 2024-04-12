# Generated by Django 4.2.7 on 2024-01-20 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
        ('Admin', '0011_tbl_gallery'),
        ('UserApp', '0004_delete_tbl_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rating', models.IntegerField(max_length=20)),
                ('user_review', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('review_datetime', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]