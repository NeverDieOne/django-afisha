from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=250, db_index=True)
    description_short = models.TextField('Короткое описание', db_index=True)
    description_long = models.TextField('Длинное описание', db_index=True)
    lat = models.CharField('Широта', max_length=50, db_index=True)
    lng = models.CharField('Долгота', max_length=50, db_index=True)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title
