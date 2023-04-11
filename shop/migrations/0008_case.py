# Generated by Django 4.1.3 on 2023-03-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_purchases_polzovatel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, db_index=True, null=True, upload_to='', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
            },
        ),
    ]