# Generated by Django 2.0.2 on 2018-04-09 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_system', '0012_auto_20180408_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetings',
            name='meeting_date',
            field=models.DateField(null=True, verbose_name='meeting date'),
        ),
    ]
