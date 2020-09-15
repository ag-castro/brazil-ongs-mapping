# Generated by Django 2.2.15 on 2020-09-14 17:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200914_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.SlugField(auto_created=True, default='zm3g25wvq7lh0latonrxukn2ve6p09u0ri9h05tuv5xyyfik6l2yre8n94v5', help_text='URL de exibição da ONG.', max_length=60, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid'), django.core.validators.RegexValidator(re.compile('^[-\\w]+\\Z'), "Enter a valid 'slug' consisting of Unicode letters, numbers, underscores, or hyphens.", 'invalid')], verbose_name='Slug'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Endereço')),
                ('number', models.IntegerField(blank=True, default=0, null=True, verbose_name='Número')),
                ('neighborhood', models.CharField(max_length=50, verbose_name='Bairro/Setor')),
                ('complement', models.CharField(max_length=150, verbose_name='Complemento')),
                ('cep', models.CharField(max_length=16, verbose_name='CEP')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='city_address', to='core.City', verbose_name='Cidade')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='state_address', to='core.Uf', verbose_name='Estado/UF')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Address', verbose_name='Endereço'),
        ),
    ]