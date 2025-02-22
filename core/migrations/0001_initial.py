# Generated by Django 4.2.4 on 2023-09-05 02:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='core',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidades', models.CharField(choices=[('UNIDADES DE ARMAZENAMENTO 1', 'UNIDADES DE ARMAZENAMENTO 1'), ('UNIDADES DE ARMAZENAMENTO 2', 'UNIDADES DE ARMAZENAMENTO 2'), ('UNIDADES DE GRADEAMENTO 1', 'UNIDADES DE GRADEAMENTO 1'), ('UNIDADES DE GRADEAMENTO 2', 'UNIDADES DE GRADEAMENTO 2')], max_length=50, verbose_name='Unidades')),
                ('STATUS_DA_UNIDADE', models.CharField(choices=[('Ativado', '🟩'), ('Desativado', '🟥')], default='Ativado', max_length=10, verbose_name='STATUS_DA_UNIDADE')),
                ('STATUS_DE_SAIDA', models.CharField(choices=[('Ativado', '🟩'), ('Manutenção', '🟨'), ('Desativado', '🟥')], default='Ativado', max_length=10, verbose_name='STATUS_DE_SAIDA')),
                ('STATUS_DE_APARELHO', models.CharField(choices=[('Ativado', '🟩'), ('Manutenção', '🟨'), ('Desativado', '🟥')], default='Ativado', max_length=10, verbose_name='STATUS_DE_APARELHO')),
                ('STATUS_DE_ENTRADA', models.CharField(choices=[('Ativado', '🟩'), ('Manutenção', '🟨'), ('Desativado', '🟥')], default='Ativado', max_length=10, verbose_name='STATUS_DE_ENTRADA')),
                ('STATUS_DO_RASPADOR_DE_GRADEAMENTO', models.CharField(choices=[('Ativado', '🟩'), ('Manutenção', '🟨'), ('Desativado', '🟥')], default='Ativado', max_length=10, verbose_name='STATUS_DO_RASPADOR')),
                ('Nivel_de_Potencia_das_Bombas', models.IntegerField(blank=True, default=None, editable=models.Q(('unidades', 'UNIDADES DE ARMAZENAMENTO 1')), null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Nivel de Potencia das Bombas')),
                ('Nivel_do_Compartimento_de_gradeamento', models.IntegerField(blank=True, default=None, editable=models.Q(('unidades', 'UNIDADES DE GRADEAMENTO 1')), null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Nivel do Compartimento de Gradeamento')),
                ('Nivel_do_Tanque', models.IntegerField(blank=True, default=None, editable=models.Q(('unidades', 'UNIDADES DE ARMAZENAMENTO 2')), null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Nivel do Tanque')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
