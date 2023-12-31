# Generated by Django 4.2.6 on 2023-10-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('owner_info', models.TextField()),
                ('employee_size', models.PositiveIntegerField()),
                ('summary', models.TextField()),
                ('headquarters_location', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('founded_date', models.DateField()),
                ('founders', models.CharField(max_length=255)),
                ('operating_status', models.BooleanField(default=True)),
                ('last_funding_type', models.CharField(max_length=255)),
                ('legal_name', models.CharField(max_length=255)),
                ('stock_symbol', models.CharField(max_length=255)),
                ('company_type', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]
