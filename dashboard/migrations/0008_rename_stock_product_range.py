# Generated by Django 4.1.7 on 2023-03-01 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_product_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='Range',
        ),
    ]