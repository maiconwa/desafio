from rest_framework import serializers
from .models import CheckCartao


class CheckCartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckCartao
        extra_kwargs = {}
        fields = ['numero_cartao']
