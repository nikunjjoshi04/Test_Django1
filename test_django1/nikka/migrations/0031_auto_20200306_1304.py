# Generated by Django 3.0.3 on 2020-03-06 13:04

import datetime
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('nikka', '0030_auto_20200304_1649'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='entry',
            managers=[
                ('ent', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateField(verbose_name=datetime.date(2020, 3, 6)),
        ),
    ]
