# Generated by Django 3.0 on 2022-02-06 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220115_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='date_create',
            field=models.DateField(verbose_name='Date Create'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
    ]
