from rest_framework import serializers
from .models import CheckCartao, FileApi

class FileApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileApi
        extra_kwargs = {'unique'}
        fields = ['nome',
                  'data',
                  'lote',
                  'quantidade_registro',
                  'numeracao_no_lote',
                  'numero_cartao']


class CheckCartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckCartao
        extra_kwargs = {}
        fields = ['numero_cartao']
