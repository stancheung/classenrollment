# Generated by Django 5.0 on 2024-01-10 06:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_customuser_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='emergency_contact_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='emergency_contact_num',
            field=models.CharField(max_length=8, null=True, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone number must contain only digits.', regex='^[0-9]+$')], verbose_name='Emergency contact number'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_num',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone number must contain only digits.', regex='^[0-9]+$')], verbose_name='Phone number'),
        ),
    ]
