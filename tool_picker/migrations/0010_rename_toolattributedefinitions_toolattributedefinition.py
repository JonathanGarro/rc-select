# Generated by Django 5.0 on 2023-12-18 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tool_picker', '0009_alter_toolattributedefinitions_cost1_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToolAttributeDefinitions',
            new_name='ToolAttributeDefinition',
        ),
    ]