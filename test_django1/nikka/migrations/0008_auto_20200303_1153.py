# Generated by Django 3.0.3 on 2020-03-03 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nikka', '0007_auto_20200303_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'get_latest_by': 'release_date'},
        ),
    ]