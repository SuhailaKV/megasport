# Generated by Django 3.2.7 on 2023-01-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_modelpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='Directions',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='Warnings',
            field=models.CharField(max_length=800),
        ),
    ]