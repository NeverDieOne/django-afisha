from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=250, db_index=True)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = HTMLField('Длинное описание', blank=True)
    lat = models.DecimalField('Широта', max_digits=10, decimal_places=7, db_index=True)
    lng = models.DecimalField('Долгота', max_digits=10, decimal_places=7, db_index=True)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE, verbose_name='Место')
    image = models.ImageField(upload_to='images', verbose_name='Фотография места')
    position = models.IntegerField('Позиция', db_index=True)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['position']

    def __str__(self):
        return f"{self.id} - {str(self.place)}"
