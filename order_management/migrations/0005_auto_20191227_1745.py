# Generated by Django 3.0.1 on 2019-12-28 01:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0004_auto_20191226_0121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid',
            new_name='completed',
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_date',
            field=models.DateField(default=datetime.date(2019, 12, 27)),
        ),
    ]