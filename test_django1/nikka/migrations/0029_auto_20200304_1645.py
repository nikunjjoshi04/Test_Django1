# Generated by Django 3.0.3 on 2020-03-04 16:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nikka', '0028_auto_20200303_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_cod', models.CharField(max_length=6, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('route_length', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateField(verbose_name=datetime.date(2020, 3, 4)),
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r_race', to='nikka.Race')),
                ('runner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r_runner', to='nikka.Parson')),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='route_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_route', to='nikka.Route'),
        ),
    ]
