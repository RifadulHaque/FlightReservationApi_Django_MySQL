# Generated by Django 4.1 on 2023-04-13 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0007_alter_reservation_flight_alter_reservation_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightApp.flight'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='passenger',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightApp.passenger'),
        ),
    ]
