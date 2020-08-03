# Generated by Django 3.0.8 on 2020-08-01 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mieter', '0014_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mieter.Documents')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mieter.Type')),
            ],
        ),
    ]
