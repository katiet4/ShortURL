# Generated by Django 2.2.6 on 2019-10-31 21:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MakeShortURL', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandfurl',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 31, 21, 11, 34, 878217, tzinfo=utc)),
        ),
    ]