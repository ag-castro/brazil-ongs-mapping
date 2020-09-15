import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.deconstruct import deconstructible
from utils.model_fields import ImageResizerField


User = get_user_model()


@deconstructible
class Image(object):
    def __init__(self, sub_path=''):
        self.path = sub_path

    def __class__(self, instance, fileneme):
        ext = fileneme.split('.')[-1]
        fileneme = f'{instance.uuid}.{ext}'
        return f'user-files/images{self.path}/{fileneme}'


image_default = Image('-original')
image_small = Image('-small')
image_medium = Image('-medium')
image_large = Image('-large')


class ImageUploader(models.Model):
    """The Uploader Images files """

    user = models.ForeignKey(
        User, default=None,
        null=True, blank=True,
        on_delete=models.DO_NOTHING
    )
    name = models.CharField(
        verbose_name='Nome',
        max_length=64,
        default=None,
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to=image_default,
        max_length=300
    )
    image_small = ImageResizerField(
        size=[350, 260],
        upload_to=image_small,
        blank=True,
        null=True,
        default=None,
        quality=90,
        max_length=300
    )
    image_medium = ImageResizerField(
        size=[420, 312],
        upload_to=image_medium,
        blank=True,
        null=True,
        default=None,
        quality=90,
        max_length=300
    )
    image_large = ImageResizerField(
        size=[1260, 936],
        upload_to=image_large,
        blank=True,
        null=True,
        default=None,
        quality=90,
        max_length=300
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.CharField(
        'UUID',
        max_length=36,
        default=None,
        null=False,
        blank=True
    )

    class Meta:
        verbose_name = 'Imagem Carregada'
        verbose_name_plural = 'Imagens Carregadas'

    def __str__(self):
        return self.uuid

    def save(self, *args, **kwargs):
        if not self.pk:
            self.uuid = str(uuid.uuid4())

        if not self.image._committed:
            #  ._file because we need the InMemoryUploadedFile instance
            self.image_small = self.image._file
            self.image_medium = self.image._file
            self.image_large = self.image._file

        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
