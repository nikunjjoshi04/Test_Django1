# Generated by Django 3.0.3 on 2020-03-03 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nikka', '0006_auto_20200303_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tb_musician', related_query_name='re_musician', to='nikka.Musician', verbose_name='related musician'),
        ),
    ]
