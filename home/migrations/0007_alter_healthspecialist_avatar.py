# Generated by Django 5.0.1 on 2024-01-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_healthspecialist_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthspecialist',
            name='avatar',
            field=models.ImageField(null=True, upload_to='medical_specialists/'),
        ),
    ]