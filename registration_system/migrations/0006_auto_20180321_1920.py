# Generated by Django 2.0.2 on 2018-03-21 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_system', '0005_auto_20180321_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingdays',
            name='day_3',
            field=models.CharField(choices=[('MONDAY', 'MONDAY'), ('TUESDAY', 'TUESDAY'), ('WEDNESDAY', 'WEDNDESDAY'), ('THURSDAY', 'THURSDAY'), ('FRIDAY', 'FRIDAY'), ('SATURDAY', 'SATURDAY'), ('SUNDAY', 'SUNDAY')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='meetingdays',
            name='day_2',
            field=models.CharField(choices=[('MONDAY', 'MONDAY'), ('TUESDAY', 'TUESDAY'), ('WEDNESDAY', 'WEDNDESDAY'), ('THURSDAY', 'THURSDAY'), ('FRIDAY', 'FRIDAY'), ('SATURDAY', 'SATURDAY'), ('SUNDAY', 'SUNDAY')], max_length=10, null=True),
        ),
    ]
