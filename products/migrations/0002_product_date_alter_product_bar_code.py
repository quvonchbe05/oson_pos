# Generated by Django 4.2.4 on 2023-08-05 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='bar_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
