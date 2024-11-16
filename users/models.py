from django.contrib.auth.models import User
from django.db import models

from scooters.models import Scooter


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(verbose_name='Баланс', default=0)
    image = models.ImageField(verbose_name='Иконка', upload_to='uploads/', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Purchase(models.Model):
    user = models.ForeignKey(Customer, verbose_name='Покупатель', on_delete=models.CASCADE)
    scooter = models.ForeignKey(Scooter, verbose_name='Самокат', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена', default=1)
    time = models.IntegerField(verbose_name='Купленное время', default=1)
    buy_time = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
