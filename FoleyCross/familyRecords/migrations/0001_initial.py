# Generated by Django 2.1.2 on 2018-10-02 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('notes', models.TextField()),
                ('date', models.DateTimeField()),
                ('city', models.CharField(max_length = 200))
            ],
        ),
    ]
