# Generated by Django 4.2.5 on 2023-11-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_vehicle_activeness_vehicle_mileage'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='fuel_amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]