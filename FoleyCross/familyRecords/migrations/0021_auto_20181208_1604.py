# Generated by Django 2.1.2 on 2018-12-08 22:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('familyRecords', '0020_auto_20181208_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 8, 22, 4, 30, 655131, tzinfo=utc)),
        ),
    ]
