from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import validate_slug
from django.core.validators import validate_unicode_slug
from mptt.models import MPTTModel, TreeForeignKey


class Cause(MPTTModel):
    """The Organization Causes model definitions"""

    title = models.CharField(
        verbose_name='Causa',
        help_text='Título da causa',
        max_length=50, unique=True
    )
    parent = TreeForeignKey(
        'self',
        verbose_name='Causa Pai',
        help_text='Selecione a Causa pai',
        related_name='children',
        db_index=True, null=True, blank=True,
        on_delete=models.DO_NOTHING
    )
    slug = models.SlugField(
        verbose_name='URL única',
        validators=[validate_slug, validate_unicode_slug],
        allow_unicode=False, unique=True
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = ['title', 'slug', ]
        verbose_name = 'Causa'
        verbose_name_plural = 'Causas'

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except ValueError:
            ancestors = []
        else:
            ancestors = [i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i + 1]))
        return slugs

    def get_absolute_url(self):
        if not self.parent:
            return reverse('main_causes_list', args=[self.slug])
        return reverse('children_causes_list',
                       args=[slugify(self.parent), self.slug])

    def __str__(self):
        return self.title
