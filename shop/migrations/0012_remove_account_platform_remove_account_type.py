# Generated by Django 4.1.3 on 2023-05-15 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_platformaccount_typeaccount_account_platform_fk_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='platform',
        ),
        migrations.RemoveField(
            model_name='account',
            name='type',
        ),
    ]
