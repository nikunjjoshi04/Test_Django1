# Generated by Django 3.0.3 on 2020-03-06 13:06

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('nikka', '0031_auto_20200306_1304'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='entry',
            managers=[
                ('o', django.db.models.manager.Manager()),
            ],
        ),
    ]