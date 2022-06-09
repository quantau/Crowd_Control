# Generated by Django 2.0.1 on 2022-03-28 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_customer_prefftime1_alter_customer_prefftime2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefftime1',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 28, 23, 9, 0, 196383), null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefftime2',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 28, 23, 9, 0, 196383), null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prefftime3',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 28, 23, 9, 0, 196383), null=True),
        ),
    ]
