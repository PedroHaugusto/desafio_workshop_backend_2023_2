from rest_framework import serializers
from .models import Funcionario, Departamento


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model =Funcionario
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Departamento
        fields = '__all__'