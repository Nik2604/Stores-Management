# Generated by Django 4.1.7 on 2023-03-30 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_rename_pname_gallery_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Electrical', 'Electrical'), ('Electronics', 'Electronics'), ('Mechaical', 'Mechanical'), ('Civil', 'Civil'), ('Computer Science', 'Computer Science')], max_length=20, null=True),
        ),
    ]
