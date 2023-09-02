from rest_framework import viewsets
from funcionariosapi.models import Departamento, Funcionario
from funcionariosapi.serializers import DepartamentoSerializer, FuncionarioSerializer

class DepartamentoViewset(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class FuncionarioViewset(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

