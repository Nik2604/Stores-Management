# Generated by Django 4.1.7 on 2023-03-01 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_addrerss_profile_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address',
            new_name='department',
        ),
    ]