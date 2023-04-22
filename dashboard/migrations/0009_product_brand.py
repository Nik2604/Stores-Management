# Generated by Django 4.1.7 on 2023-03-03 05:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_rename_stock_product_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Brand',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
