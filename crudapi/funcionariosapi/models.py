from django.db import models

class Departamento(models.Model):
    departamento = models.CharField(max_length= 50)

    def __str__(self):
        return self.departamento

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=100)
    id_funcionario = models.CharField(max_length=8, primary_key=True)
    telefone = models.CharField(max_length=15)
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.nomecompleto
    
