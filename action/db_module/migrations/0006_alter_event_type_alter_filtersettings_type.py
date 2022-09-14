# Generated by Django 4.0.3 on 2022-09-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_module', '0005_alter_event_date_alter_event_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('OTHER', 'OTHER'), ('EXHIBITION', 'EXHIBITION'), ('MUSIC', 'MUSIC'), ('MEETING', 'MEETING'), ('FESTIVAL', 'FESTIVAL'), ('ALL', 'ALL'), ('PERFORMANCE', 'PERFORMANCE')], default='OTHER', max_length=15),
        ),
        migrations.AlterField(
            model_name='filtersettings',
            name='type',
            field=models.CharField(choices=[('OTHER', 'OTHER'), ('EXHIBITION', 'EXHIBITION'), ('MUSIC', 'MUSIC'), ('MEETING', 'MEETING'), ('FESTIVAL', 'FESTIVAL'), ('ALL', 'ALL'), ('PERFORMANCE', 'PERFORMANCE')], default='ALL', max_length=15),
        ),
    ]
