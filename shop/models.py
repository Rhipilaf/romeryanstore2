from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.template.defaultfilters import safe

class Polzovatel(models.Model):
    class Meta():
        verbose_name = 'Пользователь сайта'
        verbose_name_plural = 'Пользователь сайта'
        db_table = 'polzovatel'

    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    nickname = models.CharField('Никнейм', max_length=255, blank=True, null=True)
    image = models.ImageField('Фото', null=True, blank=True)
    mail = models.EmailField('Почта', unique=True, null=True, blank=True)
class Purchases(models.Model):
    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    polzovatel = models.ForeignKey(Polzovatel, verbose_name='Пользователь', on_delete=models.CASCADE)
    account = models.CharField('Аккаунт', max_length=255)
    number_purchase = models.CharField('Номер заказа', max_length=255)
    platform = models.CharField('Платформа', max_length=255)
    login = models.CharField('Логин', max_length=255)
    password = models.CharField('Пароль', max_length=255)
    time = models.DateTimeField('Время')

    def __str__(self):
        return self.account

class TypeAccount(models.Model):
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

class PlatformAccount(models.Model):
    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'

    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name

class Account(models.Model):
    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'игры'

    title = models.CharField('Название', max_length=255)
    description = models.CharField('Описание', max_length=300)
    full_description = models.TextField('Полное описание', max_length=1500)
    price = models.CharField('Цена', max_length=255)
    availability = models.CharField('Наличие', max_length=255)
    sales = models.CharField('Кол-во продаж', max_length=255)
    genre = models.CharField('Жанр', max_length=255)
    type_fk = models.ForeignKey(TypeAccount, verbose_name='Тип', on_delete=models.SET_NULL, null=True, blank=True)
    platform_fk = models.ForeignKey(PlatformAccount, verbose_name='Платформа', on_delete=models.SET_NULL, null=True, blank=True)
    img = models.ImageField('Картинка')

    def get_img_admin(self):
        if self.img:
            return safe(
                f'<a target="_black" href="{self.img.url}"><img width=70 height=70 src="{self.img.url}"></a>')
        return 'нет'

    def __str__(self):
        return self.title

class Info(models.Model):
    title = models.CharField('Заглавие', max_length=255)
    description = models.CharField('Описание', max_length=255)
    photo = models.ImageField('Картинка', null=True, blank=True, db_index=True)

    class Meta:
        verbose_name = 'Инфо-карта'
        verbose_name_plural = 'Инфо-карты'

class Case(models.Model):
    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'

    title = models.CharField('Название', max_length=255)
    description = models.CharField('Описание', max_length=255)
    photo = models.ImageField('Картинка', null=True, blank=True, db_index=True)

class GameInCase(models.Model):

    class Meta:
        verbose_name = 'Игра в кейсе'
        verbose_name_plural = 'Игры в кейсе'

    case = models.ForeignKey(Case, verbose_name='Кейс', on_delete=models.CASCADE)
    account = models.ForeignKey(Account, verbose_name='Игра', on_delete=models.CASCADE)





