# Generated by Django 5.0 on 2024-03-04 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tool_picker', '0045_alter_toolfeature_cash_rtm_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toolfeature',
            old_name='cash_rtm_code',
            new_name='cash_RTM_code',
        ),
    ]
