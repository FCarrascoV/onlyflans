# Generated by Django 3.2.4 on 2024-07-27 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20240726_2247'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Personal',
            new_name='Staff',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='personal_uuid',
            new_name='staff_uuid',
        ),
    ]
