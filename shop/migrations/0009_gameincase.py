# Generated by Django 4.1.3 on 2023-03-05 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_case'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameInCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.account', verbose_name='Игра')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.case', verbose_name='Кейс')),
            ],
            options={
                'verbose_name': 'Игра в кейсе',
                'verbose_name_plural': 'Игры в кейсе',
            },
        ),
    ]
