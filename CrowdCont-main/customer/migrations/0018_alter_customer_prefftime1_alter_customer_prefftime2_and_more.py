# Generated by Django 4.0.3 on 2022-04-06 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_remove_customer_prefftime1_closing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='prefftime1',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefftime2',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefftime3',
            field=models.TimeField(null=True),
        ),
    ]
