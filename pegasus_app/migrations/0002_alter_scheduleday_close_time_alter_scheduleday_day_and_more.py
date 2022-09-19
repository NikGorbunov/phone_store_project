# Generated by Django 4.1.1 on 2022-09-19 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegasus_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleday',
            name='close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scheduleday',
            name='day',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=32),
        ),
        migrations.AlterField(
            model_name='scheduleday',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='scheduleday',
            name='open_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
