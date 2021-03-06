# Generated by Django 2.1.2 on 2018-10-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familyRecords', '0008_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='city',
            field=models.CharField(default='Foley', max_length=140),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_0_5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_18_24',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_25_44',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_45_64',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_65_plus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_6_17',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_active_people',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_race_asian',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_race_black',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_race_hawaiian',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_race_hispanic',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_race_nativeAm',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_race_other',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_race_two_plus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='visit',
            name='total_race_white',
            field=models.IntegerField(default=0),
        ),
    ]
