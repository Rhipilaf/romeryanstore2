from django.db import models


# Create your models here.
from django.template.defaultfilters import safe


class Purchases(models.Model):
    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    account = models.CharField('Аккаунт', max_length=255)
    number_purchase = models.CharField('Номер заказа', max_length=255)
    platform = models.CharField('Платформа', max_length=255)
    login = models.CharField('Логин', max_length=255)
    password = models.CharField('Пароль', max_length=255)
    time = models.DateTimeField('Время')

    def __str__(self):
        return self.account


class Account(models.Model):
    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'игры'

    title = models.CharField('Название', max_length=255)
    description = models.CharField('Описание', max_length=300)
    full_description = models.CharField('Полное описание', max_length=1000)
    price = models.CharField('Цена', max_length=255)
    availability = models.CharField('Наличие', max_length=255)
    sales = models.CharField('Кол-во продаж', max_length=255)
    genre = models.CharField('Жанр', max_length=255)
    platform = models.CharField('Платформа', max_length=255)
    type = models.CharField('Тип', max_length=255)
    img = models.ImageField('Картинка', null=True, blank=True, db_index=True)

    def get_img_admin(self):
        if self.img:
            return safe(
                f'<a target="_black" href="{self.img.url}"><img width=70 height=70 src="{self.img.url}"></a>')
        return 'нет'

    def __str__(self):
        return self.title
