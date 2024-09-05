# Generated by Django 5.0.7 on 2024-09-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('number_plate', models.CharField(max_length=10)),
            ],
        ),
    ]
