# Generated by Django 2.2.10 on 2020-03-10 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200310_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 10, 10, 21, 34, 303039)),
        ),
    ]
