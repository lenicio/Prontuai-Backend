from django.core.exceptions import ValidationError
from django.db import models


class Especialidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidades = models.ManyToManyField(Especialidade)

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='enderecos')
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)  # UF
    cep = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"
