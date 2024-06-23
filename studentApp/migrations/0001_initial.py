# Generated by Django 5.0.6 on 2024-06-23 16:16

import studentApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='male', max_length=10)),
                ('phone_number', models.IntegerField(unique=True, validators=[studentApp.models.validate_phone_number])),
            ],
        ),
    ]