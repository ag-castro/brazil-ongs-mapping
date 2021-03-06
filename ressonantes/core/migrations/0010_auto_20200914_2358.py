# Generated by Django 2.2.15 on 2020-09-14 23:58

import core.models.uploads
import django.core.validators
from django.db import migrations, models
import re
import utils.model_fields.image_resize_field


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200914_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageuploader',
            name='image',
            field=models.ImageField(max_length=300, upload_to=core.models.uploads.__class__('-original')),
        ),
        migrations.AlterField(
            model_name='imageuploader',
            name='image_large',
            field=utils.model_fields.image_resize_field.ImageResizerField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, max_length=300, null=True, quality=90, size=[1260, 936], upload_to=core.models.uploads.__class__('-large')),
        ),
        migrations.AlterField(
            model_name='imageuploader',
            name='image_medium',
            field=utils.model_fields.image_resize_field.ImageResizerField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, max_length=300, null=True, quality=90, size=[420, 312], upload_to=core.models.uploads.__class__('-medium')),
        ),
        migrations.AlterField(
            model_name='imageuploader',
            name='image_small',
            field=utils.model_fields.image_resize_field.ImageResizerField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, max_length=300, null=True, quality=90, size=[350, 260], upload_to=core.models.uploads.__class__('-small')),
        ),
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.SlugField(auto_created=True, default='pwgjo697jtfu9ka77xe2ctm2gcc06tze824xvvihl0mq17nppmk86ezwlt39', help_text='URL de exibição da ONG.', max_length=60, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid'), django.core.validators.RegexValidator(re.compile('^[-\\w]+\\Z'), "Enter a valid 'slug' consisting of Unicode letters, numbers, underscores, or hyphens.", 'invalid')], verbose_name='Slug'),
        ),
    ]
