# Generated by Django 4.1.3 on 2022-11-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='full_description',
            field=models.TextField(max_length=1000, verbose_name='Полное описание'),
        ),
    ]
