from django.db import models


class Address(models.Model):
    """Address model definitions"""

    address = models.CharField(
        verbose_name='Endereço',
        max_length=255,
    )
    number = models.IntegerField(
        verbose_name='Número',
        default=0,
        null=True, blank=True
    )
    neighborhood = models.CharField(
        verbose_name='Bairro/Setor',
        max_length=50,
    )
    complement = models.CharField(
        verbose_name='Complemento',
        max_length=150,
    )
    state = models.ForeignKey(
        'core.Uf', blank=False, null=False,
        verbose_name='Estado/UF',
        on_delete=models.DO_NOTHING,
        related_name='state_address'
    )
    city = models.ForeignKey(
        'core.City', blank=False, null=False,
        verbose_name='Cidade',
        on_delete=models.DO_NOTHING,
        related_name='city_address'
    )
    cep = models.CharField(
        max_length=16,
        verbose_name='CEP'
    )

    @property
    def format_address(self):
        return f'{self.address}, {self.complement} ' \
            f'Nº {self.number} - {self.neighborhood} - ' \
            f'{self.city.name} {self.state.name} - CEP {self.cep}'

    @property
    def location(self):
        return f'{self.city.name} - {self.state.name}'

    def __str__(self):
        if not self.number:
            self.number = 's/n'
        return self.format_address()
