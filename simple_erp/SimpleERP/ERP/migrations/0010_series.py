# Generated by Django 2.0 on 2018-04-21 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0009_auto_20180420_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_prefix', models.CharField(max_length=100)),
                ('series_count', models.IntegerField(default=0)),
                ('series_for', models.CharField(max_length=50)),
                ('is_default', models.BooleanField(default=True)),
                ('company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ERP.Company')),
            ],
        ),
    ]
