# Generated by Django 5.0 on 2023-12-19 18:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool_picker', '0015_toolpicker_setup_complexity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolpicker',
            name='maintenance',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Maintenance cannot be less than 1'), django.core.validators.MaxValueValidator(4, message='Maintenance cannot be greater than 4')]),
        ),
        migrations.AddField(
            model_name='toolpickerresponses',
            name='maintenance',
            field=models.IntegerField(default=0),
        ),
    ]
