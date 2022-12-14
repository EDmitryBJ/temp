# Generated by Django 4.0.3 on 2022-09-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_module', '0015_alter_event_type_alter_filtersettings_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('OTHER', 'OTHER'), ('MUSIC', 'MUSIC'), ('ALL', 'ALL'), ('FESTIVAL', 'FESTIVAL'), ('PERFORMANCE', 'PERFORMANCE'), ('EXHIBITION', 'EXHIBITION'), ('MEETING', 'MEETING')], default='OTHER', max_length=15),
        ),
        migrations.AlterField(
            model_name='filtersettings',
            name='type',
            field=models.CharField(choices=[('OTHER', 'OTHER'), ('MUSIC', 'MUSIC'), ('ALL', 'ALL'), ('FESTIVAL', 'FESTIVAL'), ('PERFORMANCE', 'PERFORMANCE'), ('EXHIBITION', 'EXHIBITION'), ('MEETING', 'MEETING')], default='ALL', max_length=15),
        ),
    ]
