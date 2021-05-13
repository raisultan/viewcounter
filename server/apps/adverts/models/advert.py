from django.db import models
from django.utils.translation import ugettext_lazy as _


class Advert(models.Model):
    title = models.CharField(
        max_length=254,
        verbose_name=_('Title'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
    )

    city = models.ForeignKey(
        to='adverts.City',
        on_delete=models.CASCADE,
        related_name='adverts',
        verbose_name=_('City'),
    )
    category = models.ForeignKey(
        to='adverts.Category',
        on_delete=models.CASCADE,
        related_name='adverts',
        verbose_name=_('Category'),
    )

    views = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Number of views'),
    )

    objects = models.Manager()

    class Meta:
        verbose_name = 'advert'
        verbose_name_plural = 'adverts'

    def __str__(self) -> str:
        return f'Advert - {self.title}'
