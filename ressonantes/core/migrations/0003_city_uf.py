# Generated by Django 2.2.15 on 2020-09-01 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200828_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=2, verbose_name='State acronym')),
                ('name', models.CharField(max_length=20, verbose_name='State name')),
                ('region', models.CharField(default='No region was given', max_length=30, verbose_name='Region name')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome da Cidade')),
                ('uf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cities_uf', to='core.Uf', verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
                'ordering': ['-name'],
            },
        ),
    ]
