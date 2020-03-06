# Generated by Django 3.0.3 on 2020-03-04 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nikka', '0029_auto_20200304_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='results',
            name='runner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r_runner', to='nikka.Runner'),
        ),
    ]