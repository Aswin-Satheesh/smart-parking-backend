# Generated by Django 5.0.7 on 2024-09-05 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='no_available',
            field=models.IntegerField(),
        ),
    ]
