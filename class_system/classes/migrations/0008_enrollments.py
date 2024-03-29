# Generated by Django 5.0 on 2024-01-06 15:09

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_alter_classes_time_slot'),
        ('users', '0004_remove_customuser_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateTimeField(default=django.utils.timezone.now)),
                ('class_enrolled', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='classes.classes')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
        ),
    ]
