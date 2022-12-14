# Generated by Django 4.0.3 on 2022-09-13 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_module', '0019_alter_event_type_alter_filtersettings_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='invited_users',
        ),
        migrations.RemoveField(
            model_name='event',
            name='is_private',
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('ALL', 'ALL'), ('EXHIBITION', 'EXHIBITION'), ('OTHER', 'OTHER'), ('FESTIVAL', 'FESTIVAL'), ('MEETING', 'MEETING'), ('MUSIC', 'MUSIC'), ('PERFORMANCE', 'PERFORMANCE')], default='OTHER', max_length=15),
        ),
        migrations.AlterField(
            model_name='filtersettings',
            name='type',
            field=models.CharField(choices=[('ALL', 'ALL'), ('EXHIBITION', 'EXHIBITION'), ('OTHER', 'OTHER'), ('FESTIVAL', 'FESTIVAL'), ('MEETING', 'MEETING'), ('MUSIC', 'MUSIC'), ('PERFORMANCE', 'PERFORMANCE')], default='ALL', max_length=15),
        ),
    ]
