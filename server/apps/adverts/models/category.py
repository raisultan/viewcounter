from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        max_length=254,
        verbose_name=_('Name'),
    )

    objects = models.Manager()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return f'Category - {self.name}'
