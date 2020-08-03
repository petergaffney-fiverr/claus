# Generated by Django 2.1.5 on 2020-07-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mieter', '0005_familienstand_mieterpersonfamilienstand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mieterperson',
            name='anschrift_hausnummer',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='anschrift_plz',
            field=models.CharField(blank=True, default=None, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='anschrift_stadt',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='anschrift_strasse',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='arbeitgeber_anschrift',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='arbeitgeber_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Dezeitiger Arbeitgeber'),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='arbeitgeber_telefonnummer',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='arbeitsgeber_datum_besch',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='beruf',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Ausgeübter Beruf'),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='einkommen',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Mtl. Nettoeinkommen'),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='geburtsdatum',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='nachname',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='vermieter_anschrift',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='vermieter_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='vermieter_telefonnummer',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='mieterperson',
            name='vorname',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]