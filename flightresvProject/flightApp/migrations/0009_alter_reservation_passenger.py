# Generated by Django 4.1 on 2023-04-14 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0008_alter_reservation_flight_alter_reservation_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightApp.passenger'),
        ),
    ]
