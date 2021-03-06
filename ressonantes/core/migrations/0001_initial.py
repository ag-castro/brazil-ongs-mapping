# Generated by Django 2.2.15 on 2020-08-28 20:37

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(help_text='Define o primeiro nome do usuário.', max_length=50, verbose_name='Nome')),
                ('last_name', models.CharField(help_text='Define o sobre-nome do usuário.', max_length=50, verbose_name='Sobre-nome')),
                ('email', models.EmailField(help_text='Define o e-mail de acesso do usuário', max_length=254, unique=True, verbose_name='E-mail')),
                ('mobile', models.CharField(max_length=25, unique=True, verbose_name='Nº Celular')),
                ('is_whatsapp_mobile', models.BooleanField(default=True, verbose_name='Celular com WhatsApp?')),
                ('is_ong', models.BooleanField(default=False, help_text='Define o usuário como uma ONG.', verbose_name='É uma ONG?')),
                ('is_staff', models.BooleanField(default=False, help_text='Define se o usuário é membro da equipe Ressonantes.', verbose_name='Membro da Equipe?')),
                ('is_active', models.BooleanField(default=True, help_text='Habilita ou Desabilita o usuário na aplicação.', verbose_name='Usuário Habilitado?')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Data da realização do cadastro.', verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Data da atualização mais recente.', verbose_name='Atualizado em')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ['-updated_at', django.db.models.expressions.OrderBy(django.db.models.expressions.F('first_name'), nulls_last=True)],
                'unique_together': {('email', 'mobile')},
            },
        ),
    ]
