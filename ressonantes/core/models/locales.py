from django.db import models
from django.utils.translation import gettext_lazy as _
from core.managers import CityManager


class Uf(models.Model):
    """Brazilian States UFs model"""

    acronym = models.CharField(
        blank=False, max_length=2,
        null=False, verbose_name=_('State acronym')
    )
    name = models.CharField(
        blank=False, max_length=20,
        null=False, verbose_name=_('State name')
    )
    region = models.CharField(
        blank=False, default=_('No region was given'),
        max_length=30,
        null=False, verbose_name=_('Region name')
    )

    objects = models.Manager()

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')
        ordering = ['name']

    def __str__(self):
        return self.name


class City(models.Model):
    """Brazilian City Model"""

    uf = models.ForeignKey(
        'core.Uf', null=True,
        related_name='cities_uf',
        verbose_name='Estado',
        on_delete=models.SET_NULL
    )
    name = models.CharField(
        blank=False, max_length=100,
        null=False, verbose_name='Nome da Cidade'
    )

    objects = CityManager()

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['-name']

    def __str__(self):
        return self.name
