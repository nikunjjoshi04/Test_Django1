# Generated by Django 3.0.3 on 2020-03-03 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nikka', '0023_auto_20200303_1542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['birth_date'], 'permissions': [('can_learn', 'Can Learn')]},
        ),
    ]
