# Generated by Django 5.0.7 on 2024-09-06 03:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0008_parking'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='number_plate',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='numberPlate', to='features.user'),
            preserve_default=False,
        ),
    ]
