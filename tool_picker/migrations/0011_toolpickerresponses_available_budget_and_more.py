# Generated by Django 5.0 on 2023-12-18 18:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool_picker', '0010_rename_toolattributedefinitions_toolattributedefinition'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolpickerresponses',
            name='available_budget',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='toolpickerresponses',
            name='intended_use_type',
            field=models.CharField(default='No data provided.', max_length=50),
        ),
        migrations.AlterField(
            model_name='toolpicker',
            name='available_budget',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0, message='Available budget cannot be less than 1'), django.core.validators.MaxValueValidator(4, message='Available budget cannot be greater than 4')]),
        ),
    ]
