# Generated by Django 4.2.4 on 2023-08-05 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_date_alter_product_bar_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
    ]