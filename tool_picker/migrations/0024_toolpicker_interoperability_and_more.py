# Generated by Django 5.0 on 2023-12-19 19:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool_picker', '0023_toolpicker_data_viz_toolpickerresponses_data_viz'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolpicker',
            name='interoperability',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Interoperability cannot be less than 1'), django.core.validators.MaxValueValidator(4, message='Interoperability cannot be greater than 4')]),
        ),
        migrations.AddField(
            model_name='toolpickerresponses',
            name='interoperability',
            field=models.IntegerField(default=0),
        ),
    ]
