# Generated by Django 4.1.3 on 2023-03-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_gameincase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='img',
            field=models.ImageField(default=1, upload_to='', verbose_name='Картинка'),
            preserve_default=False,
        ),
    ]
