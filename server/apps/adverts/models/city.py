from django.db import models
from django.utils.translation import ugettext_lazy as _


class City(models.Model):
    name = models.CharField(
        max_length=254,
        verbose_name=_('Name'),
    )

    objects = models.Manager()

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self) -> str:
        return f'City - {self.name}'
