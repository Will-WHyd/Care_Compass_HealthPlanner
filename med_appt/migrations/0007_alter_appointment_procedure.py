# Generated by Django 4.2.16 on 2024-11-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_appt', '0006_alter_appointment_appt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='procedure',
            field=models.CharField(max_length=200),
        ),
    ]
