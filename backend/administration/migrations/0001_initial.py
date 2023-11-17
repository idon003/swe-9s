# Generated by Django 4.2.5 on 2023-11-17 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0003_vehicle_fuel_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_performance', models.TextField()),
                ('fuel_performance', models.TextField()),
                ('maintenance_performance', models.TextField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
    ]
