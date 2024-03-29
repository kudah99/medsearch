# Generated by Django 5.0.1 on 2024-01-12 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_healthfacilitycategory_remove_city_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalSpecialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HealthSpecialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('professional_title', models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.'), ('DR', 'Dr.'), ('PROF', 'Prof.')], default='MR', max_length=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.city')),
                ('contact_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.contact')),
                ('medical_specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.medicalspecialty')),
            ],
        ),
    ]
