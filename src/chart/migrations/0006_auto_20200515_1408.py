# Generated by Django 2.1.5 on 2020-05-15 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0005_schedule_o_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='o_number',
            new_name='receipt_number',
        ),
    ]
