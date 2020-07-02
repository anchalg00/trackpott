# Generated by Django 2.1.5 on 2020-06-25 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0010_auto_20200515_2149'),
        ('projects', '0009_scheduledocument_scheduleinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleinfo',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chart.Schedule'),
        ),
    ]