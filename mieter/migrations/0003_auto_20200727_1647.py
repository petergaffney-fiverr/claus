# Generated by Django 2.1.5 on 2020-07-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mieter', '0002_mieterperson_telefonnummer'),
    ]

    operations = [
        migrations.AddField(
            model_name='mieterperson',
            name='arbeitgeber_festanstellung',
            field=models.BooleanField(blank=True, choices=[(None, 'N/A'), (True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='mieterperson',
            name='arbeitgeber_probezeit',
            field=models.BooleanField(blank=True, choices=[(None, 'N/A'), (True, 'Yes'), (False, 'No')], default=None, null=True),
        ),
    ]
