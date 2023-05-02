from rest_framework import serializers

from .models import *

class EstanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estante
        fields = '__all__'

class RepisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repisa
        fields = '__all__'

class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'nombre':instance.nombre,
            'autor':instance.autor,
            'descripcion': instance.descripcion,
            'estante':instance.estante.estante,
            'Repisa':instance.repisa.repisa
        }