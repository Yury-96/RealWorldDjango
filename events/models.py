from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200,  # максимальная длина поля
                             default='',  # значение по умолчанию для новых объектов
                             verbose_name='Название'  # название, выводимое на сайте
                             )

    class Meta:
        ordering = ['-title']  # сортировка
        verbose_name_plural = 'События'  # форма единственного числа
        verbose_name = 'Событие'  # форма множественного числа

    description = models.TextField(#max_length=1000,#None,  # максимальная длина поля
                             default='',  # значение по умолчанию для новых объектов
                             verbose_name='Описание'  # название, выводимое на сайте
                             )

    date_start = models.DateTimeField(verbose_name='Дата начала')

    participants_number = models.PositiveSmallIntegerField(verbose_name='Количество участников')

    is_private = models.BooleanField(default=False,  # значение по умолчанию для новых объектов
                             verbose_name='Частное'  # название, выводимое на сайте
                             )

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=90,  # максимальная длина поля
                             default='',  # значение по умолчанию для новых объектов
                             verbose_name='Категория'  # название, выводимое на сайте
                             )

    class Meta:
        ordering = ['-title']  # сортировка
        verbose_name_plural = 'Категории'  # форма единственного числа
        verbose_name = 'Категория'  # форма множественного числа

    def __str__(self):
        return self.title