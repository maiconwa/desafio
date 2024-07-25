from django.db import models

# Create your models here.


class FileApi(models.Model):
    nome = models.CharField(blank=True, default=None, null=True, max_length=30, help_text='NOME')
    data = models.DateField(blank=True, default=None, null=True, max_length=8, help_text='DATA')
    lote = models.CharField(blank=True, default=None, null=True, max_length=8, help_text='LOTE')
    quantidade_registro = models.CharField(blank=True, default=None, null=True, max_length=6, help_text='QDT DE REGISTROS')
    numeracao_no_lote = models.CharField(blank=True, default=None, null=True, max_length=8, help_text='NUMERAÇÃO NO LOTE')
    numero_cartao = models.CharField(blank=True, default=None, null=True, max_length=500, help_text='NUMERO DE CARTÃO COMPLETO')
    unique = models.CharField(blank=True, default=None, null=True, max_length=30, help_text='IDENTIFICADOR UNICO')


class CheckCartao(models.Model):
    numero_cartao = models.CharField(blank=True, default=None, null=True, max_length=50, help_text='NUMERO DE CARTÃO COMPLETO')
