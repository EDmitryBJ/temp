# Generated by Django 4.0.3 on 2022-09-09 06:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('db_module', '0013_userprofile_subscribers_num_alter_event_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('MUSIC', 'MUSIC'), ('MEETING', 'MEETING'), ('PERFORMANCE', 'PERFORMANCE'), ('EXHIBITION', 'EXHIBITION'), ('ALL', 'ALL'), ('FESTIVAL', 'FESTIVAL'), ('OTHER', 'OTHER')], default='OTHER', max_length=15),
        ),
        migrations.AlterField(
            model_name='filtersettings',
            name='type',
            field=models.CharField(choices=[('MUSIC', 'MUSIC'), ('MEETING', 'MEETING'), ('PERFORMANCE', 'PERFORMANCE'), ('EXHIBITION', 'EXHIBITION'), ('ALL', 'ALL'), ('FESTIVAL', 'FESTIVAL'), ('OTHER', 'OTHER')], default='ALL', max_length=15),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
    ]
