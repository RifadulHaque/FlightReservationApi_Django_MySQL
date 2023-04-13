# Generated by Django 4.1 on 2023-04-13 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0004_alter_reservation_flight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reservationNumber',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='passenger',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flightApp.passenger'),
        ),
    ]