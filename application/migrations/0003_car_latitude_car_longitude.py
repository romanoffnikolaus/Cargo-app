# Generated by Django 4.2.1 on 2023-05-26 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_car_application_current_0fcc8a_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=9, null=True),
        ),
    ]
