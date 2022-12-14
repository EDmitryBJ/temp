# Generated by Django 4.0.3 on 2022-09-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_module', '0003_alter_contacts_email_alter_contacts_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('ALL', 'ALL'), ('MEETING', 'MEETING'), ('PERFORMANCE', 'PERFORMANCE'), ('MUSIC', 'MUSIC'), ('OTHER', 'OTHER'), ('EXHIBITION', 'EXHIBITION'), ('FESTIVAL', 'FESTIVAL')], default='OTHER', max_length=15),
        ),
        migrations.AlterField(
            model_name='filtersettings',
            name='type',
            field=models.CharField(choices=[('ALL', 'ALL'), ('MEETING', 'MEETING'), ('PERFORMANCE', 'PERFORMANCE'), ('MUSIC', 'MUSIC'), ('OTHER', 'OTHER'), ('EXHIBITION', 'EXHIBITION'), ('FESTIVAL', 'FESTIVAL')], default='ALL', max_length=15),
        ),
    ]
