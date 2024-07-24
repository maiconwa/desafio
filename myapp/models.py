from django.db import models

# Create your models here.
class FileApi(models.Model):
    nome = models.CharField(blank=True, default=None, max_length=30, help_text='NOME')
    data = models.DateField(blank=True, default=None, max_length=8, help_text='DATA')
    lote = models.CharField(blank=True, default=None, max_length=8, help_text='LOTE')
    qtdregistro = models.CharField(blank=True, default=None, max_length=6, help_text='QDT DE REGISTROS')
    numlote = models.CharField(blank=True, default=None, max_length=8, help_text='NUMERAÇÃO DO LOTE')
    numcartao = models.IntegerField(blank=True, default=None, max_length=19, help_text='NUMERO DE CARTÃO COMPLETO')
    