# Generated by Django 2.2.5 on 2021-01-10 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20210109_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calendar', to='reservation.Clinic'),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='departments',
            field=models.ManyToManyField(related_name='clinics', to='reservation.Department'),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='doctors',
            field=models.ManyToManyField(related_name='clinics', through='reservation.DoctorClinicRelation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_patient', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_frame',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='reservation.ReservationFrame'),
        ),
        migrations.AlterField(
            model_name='reservationframe',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_frames', to='reservation.Clinic'),
        ),
        migrations.AlterField(
            model_name='reservationframe',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_doctor', related_query_name='', to=settings.AUTH_USER_MODEL),
        ),
    ]
