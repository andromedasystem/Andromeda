# Generated by Django 2.0.2 on 2018-03-29 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_system', '0008_semester_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('A-', 'A-'), ('B', 'B'), ('B-', 'B-'), ('C', 'C'), ('C-', 'C-'), ('D', 'D'), ('D-', 'D-'), ('F', 'F'), ('W', 'W'), ('I', 'I'), ('NA', 'NA')], default='NA', max_length=2),
        ),
        migrations.AlterField(
            model_name='semester',
            name='status',
            field=models.CharField(choices=[('OPEN_GRADING', 'OPEN_GRADING'), ('CLOSE', 'CLOSE'), ('OPEN_REGISTRATION', 'OPEN_REGISTRATION')], default='CLOSE', max_length=35),
        ),
    ]
