# Generated by Django 3.0.8 on 2020-08-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mieter', '0016_remove_documents_doc_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beziehung',
            options={'ordering': ('beziehung',)},
        ),
        migrations.AlterModelOptions(
            name='familienstand',
            options={'ordering': ('familienstand',)},
        ),
        migrations.AlterModelOptions(
            name='stadtteil',
            options={'ordering': ('stadtteil',)},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ('type',)},
        ),
        migrations.AlterModelOptions(
            name='wohnungstyp',
            options={'ordering': ('wohnungstyp',)},
        ),
        migrations.AlterField(
            model_name='wunschwohnung',
            name='aktiv',
            field=models.BooleanField(blank=True, choices=[(None, 'N/A'), (True, 'Yes'), (False, 'No')], default=False, null=True, verbose_name='Gibt an, ob Gesuch aktiv ist'),
        ),
    ]
