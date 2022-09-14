# Generated by Django 4.0.3 on 2022-09-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('MEETING', 'MEETING'), ('PERFORMANCE', 'PERFORMANCE'), ('OTHER', 'OTHER'), ('FESTIVAL', 'FESTIVAL'), ('EXHIBITION', 'EXHIBITION'), ('MUSIC', 'MUSIC'), ('ALL', 'ALL')], default='OTHER', max_length=15),
        ),
        migrations.AlterField(
            model_name='filtersettings',
            name='type',
            field=models.CharField(choices=[('MEETING', 'MEETING'), ('PERFORMANCE', 'PERFORMANCE'), ('OTHER', 'OTHER'), ('FESTIVAL', 'FESTIVAL'), ('EXHIBITION', 'EXHIBITION'), ('MUSIC', 'MUSIC'), ('ALL', 'ALL')], default='ALL', max_length=15),
        ),
    ]
