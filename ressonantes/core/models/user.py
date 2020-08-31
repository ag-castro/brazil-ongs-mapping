from django.db import models
from django.db.models import F
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_email
from core.managers import UserRessonanteManager


class User(AbstractBaseUser, PermissionsMixin):
    """User Model Setup to the app Ressonantes"""

    first_name = models.CharField(
        blank=False, null=False,
        help_text='Define o primeiro nome do usuário.',
        max_length=50, verbose_name='Nome'
    )
    last_name = models.CharField(
        blank=False, null=False,
        help_text='Define o sobre-nome do usuário.',
        max_length=50, verbose_name='Sobre-nome'
    )
    email = models.EmailField(
        blank=False, null=False,
        help_text='Define o e-mail de acesso do usuário',
        verbose_name='E-mail', unique=True,
        validators=[validate_email]
    )
    mobile = models.CharField(
        blank=False, null=False, max_length=25,
        verbose_name='Nº Celular', unique=True,
    )
    is_whatsapp_mobile = models.BooleanField(
        default=True, verbose_name='Celular com WhatsApp?'
    )
    is_ong = models.BooleanField(
        default=False, verbose_name='É uma ONG?',
        help_text='Define o usuário como uma ONG.'
    )
    is_staff = models.BooleanField(
        default=False, verbose_name='Membro da Equipe?',
        help_text='Define se o usuário é membro da equipe Ressonantes.'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Usuário Habilitado?',
        help_text='Habilita ou Desabilita o usuário na aplicação.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em',
        help_text='Data da realização do cadastro.'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Atualizado em',
        help_text='Data da atualização mais recente.'
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = EMAIL_FIELD
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

    objects = UserRessonanteManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-updated_at', F('first_name').asc(nulls_last=True)]
        unique_together = ['email', 'mobile']

    def clean(self):
        super(User, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} <{self.email}>'
