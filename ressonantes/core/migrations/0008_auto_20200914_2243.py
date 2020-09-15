# Generated by Django 2.2.15 on 2020-09-14 22:43

import core.models.uploads
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re
import utils.model_fields.image_resize_field


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200914_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.SlugField(auto_created=True, default='ju96aq5pi709kqva0hu8c2tpxhyprpphx606324kufzzcw39pmqzw4trsuj8', help_text='URL de exibição da ONG.', max_length=60, unique=True, validators=[django.core.validators.RegexValidator(re.compile(
                '^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid'), django.core.validators.RegexValidator(re.compile('^[-\\w]+\\Z'), "Enter a valid 'slug' consisting of Unicode letters, numbers, underscores, or hyphens.", 'invalid')], verbose_name='Slug'),
        ),
        migrations.CreateModel(
            name='ImageUploader',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None,
                                          max_length=64, null=True, verbose_name='Nome')),
                ('image', models.ImageField(max_length=300,
                                            upload_to=core.models.uploads.__class__('-default'), verbose_name='Imagem')),
                ('image_small', utils.model_fields.image_resize_field.ImageResizerField(blank=True, crop=None, default=None, force_format=None,
                                                                                        keep_meta=True, max_length=300, null=True, quality=90, size=[350, 260], upload_to=core.models.uploads.__class__('-small'))),
                ('image_medium', utils.model_fields.image_resize_field.ImageResizerField(blank=True, crop=None, default=None, force_format=None,
                                                                                         keep_meta=True, max_length=300, null=True, quality=90, size=[420, 312], upload_to=core.models.uploads.__class__('-medium'))),
                ('image_large', utils.model_fields.image_resize_field.ImageResizerField(blank=True, crop=None, default=None, force_format=None,
                                                                                        keep_meta=True, max_length=300, null=True, quality=90, size=[1260, 936], upload_to=core.models.uploads.__class__('-large'))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.CharField(blank=True, default=None,
                                          max_length=36, verbose_name='UUID')),
                ('user', models.ForeignKey(blank=True, default=None, null=True,
                                           on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Imagem Carregada',
                'verbose_name_plural': 'Imagens Carregadas',
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='cover_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    related_name='coverimage_ong', to='core.ImageUploader', verbose_name='Imagem da Capa'),
        ),
        migrations.AddField(
            model_name='organization',
            name='logo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    related_name='logomarca_ong', to='core.ImageUploader', verbose_name='Logomarca da ONG'),
        ),
    ]