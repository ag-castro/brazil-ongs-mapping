from django.db import models


class SocialNetwork(models.Model):
    """Social Network model definitions"""

    DEFAULT_SOCIALNETWORKS = (
        (0, 'FaceBook'),
        (1, 'Instagram'),
        (2, 'Linkedin'),
        (3, 'Twitter'),
        (4, 'YouTube'),
    )

    title = models.CharField(
        verbose_name='Rede Social',
        max_length=50,
        choices=DEFAULT_SOCIALNETWORKS
    )
    url = models.URLField(
        unique=True, null=True, blank=True,
        verbose_name='URL do Perfil',
        help_text='Link do Perfil na rede social escolhida.',
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'

    def __str__(self):
        return self.title
