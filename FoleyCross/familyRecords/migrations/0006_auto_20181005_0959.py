# Generated by Django 2.1.2 on 2018-10-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familyRecords', '0005_auto_20181004_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(default='', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='race',
            field=models.CharField(default='', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='service',
            field=models.CharField(default='', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.CharField(default='', max_length=140),
            preserve_default=False,
        ),
    ]