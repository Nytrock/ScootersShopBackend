from django.db import models

class Scooter(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='uploads/', null=True, blank=True)
    price = models.IntegerField(verbose_name='Цена', default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Самокат'
        verbose_name_plural = 'Самокаты'
