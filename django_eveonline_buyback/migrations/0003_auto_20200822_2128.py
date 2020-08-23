# Generated by Django 2.2.10 on 2020-08-22 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_eveonline_connector', '0001_initial'),
        ('django_eveonline_buyback', '0002_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='buybacksettings',
            name='character_handlers',
            field=models.ManyToManyField(blank=True, to='django_eveonline_connector.EveCharacter'),
        ),
        migrations.AddField(
            model_name='buybacksettings',
            name='contract_corporation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_eveonline_connector.EveCorporation'),
        ),
    ]
