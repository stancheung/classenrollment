# Generated by Django 5.0 on 2024-01-25 08:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0013_alter_classes_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 25, 8, 50, 34, 956067, tzinfo=datetime.timezone.utc)),
        ),
    ]
