# Generated by Django 2.1.5 on 2020-07-27 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mieter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mieterperson',
            name='telefonnummer',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
