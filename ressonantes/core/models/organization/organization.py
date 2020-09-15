import random
import string
from datetime import date
from django.db import models
from django.core.validators import validate_email
from django.core.validators import validate_slug
from django.core.validators import validate_unicode_slug
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from utils.validators.identity.validator import IdentityValidator


User = get_user_model()


class Organization(models.Model):
    """Organization Model definitions"""

    owner = models.ForeignKey(
        User,
        verbose_name=_('Owner'),
        related_name="organizations",
        on_delete=models.DO_NOTHING
    )
    cnpj = models.CharField(
        verbose_name='CNPJ',
        blank=True, null=True,
        max_length=30, unique=True,
        validators=[IdentityValidator()]
    )
    name = models.CharField(
        unique=True,
        verbose_name='Nome da Organização',
        max_length=150, blank=False, null=False,
    )
    intro = models.CharField(
        max_length=255, verbose_name='Apresentação',
        blank=False, null=False
    )
    about = models.TextField(
        verbose_name='Sobre a Organização',
        blank=False, null=False
    )
    founder = models.CharField(
        max_length=150, blank=False, null=False,
        verbose_name='Fundador',
    )
    founded_at = models.IntegerField(
        null=False, blank=False, verbose_name='Desde',
        help_text='Ano em que a Organização foi fundada.',
        choices=[(i, i) for i in range(1900, date.today().year + 1)],
    )
    causes = models.ManyToManyField(
        'core.Cause', blank=True,
        verbose_name='Causas',
        related_name='organization_causes'
    )
    address = models.OneToOneField(
        'core.Address', blank=True, null=True,
        verbose_name='Endereço',
        on_delete=models.DO_NOTHING,
    )
    website = models.URLField(
        blank=True, null=True,
        verbose_name='Web Site',
        help_text='Digite a URL completa do web site.'
    )
    email = models.EmailField(
        blank=True, null=True,
        verbose_name='E-mail para Contatos',
        help_text='Digite um e-mail válido.'
    )
    members = models.ManyToManyField(
        'core.Member',
        verbose_name='Membros',
        blank=True
    )
    social_networks = models.ManyToManyField(
        'core.SocialNetwork',
        verbose_name='Membros',
        blank=True
    )
    slug = models.SlugField(
        verbose_name='Slug', max_length=60,
        help_text='URL de exibição da ONG.',
        unique=True, null=False, blank=False,
        auto_created=True, allow_unicode=False,
        validators=[validate_slug, validate_unicode_slug],
        default=''.join(
            random.choice(string.ascii_lowercase + string.digits)
            for _ in range(60))
    )
    created_at = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Editado em',
        auto_now=True
    )
    logo = models.ForeignKey(
        'core.ImageUploader',
        on_delete=models.DO_NOTHING, null=True,
        verbose_name='Logomarca da ONG',
        related_name='logomarca_ong'
    )
    cover_image = models.ForeignKey(
        'core.ImageUploader',
        on_delete=models.DO_NOTHING, null=True,
        verbose_name='Imagem da Capa',
        related_name='coverimage_ong'
    )

    # Date
    created_at = models.DateTimeField(
        verbose_name='Criado em', auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Editado em', auto_now=True
    )
