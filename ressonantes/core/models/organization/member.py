from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Member(models.Model):
    """Organizations Member model definitions"""

    user = models.ForeignKey(
        'core.User',
        verbose_name='Usuário', blank=True,
        related_name='user_organization_member',
        on_delete=models.DO_NOTHING
    )
    position = models.CharField(
        verbose_name='Atividade/Cargo',
        help_text='Atividades que o membro realiza.',
        max_length=150, blank=False
    )
    be_since = models.DateField(
        verbose_name='Membro Desde',
        blank=False,
    )
    social_networks = models.ManyToManyField(
        'core.SocialNetwork',
        verbose_name='Redes Sociais',
        blank=True
    )

    class Meta:
        ordering = ['be_since', 'user']
        verbose_name = 'Membro da Organização'
        verbose_name_plural = 'Membros das Organizações'

    def __str__(self):
        return self.user
