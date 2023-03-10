# Generated by Django 3.2.7 on 2022-12-31 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=200)),
                ('Net_weight', models.CharField(max_length=200)),
                ('Directions', models.CharField(max_length=200)),
                ('Warnings', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_name', models.CharField(max_length=200)),
                ('value1', models.CharField(max_length=200)),
                ('value2', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.products')),
            ],
        ),
    ]
