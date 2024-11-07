from django.db import models
from django.db.models.fields import CharField, TextField
from django.contrib.auth.models import User


class Aluno(models.Model):
  nome = models.CharField(max_length=100)
  idaluno = models.IntegerField()
  
  def agendaraula(professor):
    pass
  def avaliarprof(professor):
    pass


  def __str__(self):
    return f'{self.nome}{self.idaluno}'


class Aula(models.Model):
    idAula = models.IntegerField()
    dataAula = models.DateField()
    def __str__(self):
      return f"idAula"
    
class Professor(models.Model):
  idProfessor = models.IntegerField
  especialidade = models.CharField(max_length=200)


  def criarPerfil():
    pass
  def darAula():
    pass
  

class Avaliacao:
  idAvaliacao = models.IntegerField
  nome = models.FloatField()

  def enviar():
    pass