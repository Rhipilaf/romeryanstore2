# Generated by Django 4.1.3 on 2022-11-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_account_full_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='full_description',
            field=models.TextField(max_length=1500, verbose_name='Полное описание'),
        ),
    ]
