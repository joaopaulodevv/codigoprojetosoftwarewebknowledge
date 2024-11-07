from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idaluno = models.IntegerField()

    def agendaraula(self, professor):

        pass

    def avaliarprof(self, professor):
      
        pass

    def __str__(self):
        return f'{self.nome} ({self.idaluno})'


class Professor(models.Model):
    idProfessor = models.IntegerField()  
    especialidade = models.CharField(max_length=200)

    def criarPerfil(self):
        
        pass

    def darAula(self):
        
        pass

    def __str__(self):
        return f'Professor {self.idProfessor} - Especialidade: {self.especialidade}'


class Aula(models.Model):
    idAula = models.IntegerField()
    dataAula = models.DateField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return f'Aula {self.idAula} - {self.dataAula}'


class Avaliacao(models.Model):  
    idAvaliacao = models.IntegerField()  
    nota = models.FloatField()  

    def enviar(self):
        
        pass

    def __str__(self):
        return f'Avaliacao {self.idAvaliacao} - Nota: {self.nota}'

