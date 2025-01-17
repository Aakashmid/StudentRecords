# Generated by Django 5.0.6 on 2024-06-29 13:19

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('enrollment_date', models.DateField(auto_now_add=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, validators=[studentApp.models.validate_phone_number])),
                ('address', models.TextField(blank=True, null=True)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
    ]
