# Generated by Django 5.0 on 2024-01-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_customuser_name_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.CharField(choices=[('4-7', '4-7'), ('8-11', '8-11')], max_length=5, null=True),
        ),
    ]
