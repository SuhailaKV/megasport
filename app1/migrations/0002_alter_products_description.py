# Generated by Django 3.2.7 on 2022-12-31 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Description',
            field=models.CharField(max_length=500),
        ),
    ]
