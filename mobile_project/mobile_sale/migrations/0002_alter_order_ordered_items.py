# Generated by Django 5.1.4 on 2025-01-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_sale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_items',
            field=models.CharField(max_length=2050),
        ),
    ]
