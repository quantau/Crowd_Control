# Generated by Django 4.0.3 on 2022-03-29 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_auto_20220328_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefftime1',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 29, 16, 31, 9, 860111), null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefftime2',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 29, 16, 31, 9, 860126), null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefftime3',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 29, 16, 31, 9, 860137), null=True),
        ),
    ]
