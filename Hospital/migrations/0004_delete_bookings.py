# Generated by Django 5.0.2 on 2024-02-26 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0003_remove_bookings_date_and_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bookings',
        ),
    ]
