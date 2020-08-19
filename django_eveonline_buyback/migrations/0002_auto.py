# Generated by Django 2.2.13 on 2020-08-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_eveonline_buyback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buybacksettings',
            name='ancient_coordinates_database_price',
            field=models.FloatField(default=1500000),
        ),
        migrations.AlterField(
            model_name='buybacksettings',
            name='sleeper_drone_ai_nexus_price',
            field=models.FloatField(default=5000000),
        ),
    ]