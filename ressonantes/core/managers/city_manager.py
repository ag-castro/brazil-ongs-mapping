from django.db import models


class CityManager(models.Manager):
    """ City objects manager """

    def get_uf_cities(self, uf):
        return self.get_queryset().filter(uf__id=uf)
