# Generated by Django 2.0.2 on 2018-03-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_system', '0007_auto_20180322_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='status',
            field=models.CharField(choices=[('OPEN_GRADING', 'OPEN_GRADING'), ('CLOSE', 'CLOSE'), ('OPEN_REGISRATION', 'OPEN_REGISTRATION')], default='CLOSE', max_length=35),
        ),
    ]
