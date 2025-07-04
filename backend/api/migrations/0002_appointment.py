# Generated by Django 5.2.3 on 2025-06-26 08:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('phone_number', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('time_slot', models.CharField(choices=[('10:00-10:30', '10:00 AM - 10:30 AM'), ('10:30-11:00', '10:30 AM - 11:00 AM'), ('11:00-11:30', '11:00 AM - 11:30 AM'), ('11:30-12:00', '11:30 AM - 12:00 PM'), ('12:00-12:30', '12:00 PM - 12:30 PM'), ('12:30-13:00', '12:30 PM - 1:00 PM'), ('14:00-14:30', '2:00 pM - 2:30 PM'), ('14:30-15:00', '2:30 PM - 3:00 PM'), ('15:00-15:30', '3:00 PM - 3:30 PM'), ('15:30-16:00', '3:30 PM - 4:00 PM'), ('16:00-16:30', '4:00 PM - 4:30 PM'), ('16:30-17:00', '4:30 PM - 5:00 PM')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('date', 'time_slot')},
            },
        ),
    ]
