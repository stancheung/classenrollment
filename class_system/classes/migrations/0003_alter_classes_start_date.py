# Generated by Django 5.0 on 2023-12-27 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_classes_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='start_date',
            field=models.DateTimeField(default=datetime.date(2023, 12, 27)),
        ),
    ]
