# Generated by Django 2.1.5 on 2020-07-29 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mieter', '0007_documents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documents',
            old_name='file',
            new_name='location',
        ),
    ]