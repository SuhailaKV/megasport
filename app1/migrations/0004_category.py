# Generated by Django 3.2.7 on 2023-01-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20230106_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
            ],
        ),
    ]
