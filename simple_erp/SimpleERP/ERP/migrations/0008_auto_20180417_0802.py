# Generated by Django 2.0 on 2018-04-17 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0007_auto_20180417_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockentry',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ERP.Company'),
        ),
        migrations.AddField(
            model_name='stockentry_items',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ERP.Company'),
        ),
    ]