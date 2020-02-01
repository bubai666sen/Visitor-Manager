# Generated by Django 2.2 on 2020-02-01 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profile', '0003_auto_20200125_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='arrival',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Arrival Time'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='departure',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Departure Time'),
        ),
    ]
