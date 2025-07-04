# Generated by Django 5.2.1 on 2025-05-12 02:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=250)),
                ('tradingName', models.CharField(blank=True, max_length=250, null=True)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('stateRegistration', models.CharField(blank=True, max_length=30, null=True)),
                ('companyEmail', models.EmailField(max_length=254)),
                ('companyPhone', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=9)),
                ('address', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=10)),
                ('complement', models.CharField(blank=True, max_length=255, null=True)),
                ('neighborhood', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
