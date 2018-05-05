from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Agenda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    TIPO_CHOICES = (
        ('Publica', 'Pública'),
        ('Privada', 'Privada'),
        ('Institucional','Institucional')
    )
    tipo = models.CharField(max_length=14, choices=TIPO_CHOICES, blank=False, null=False)

    def __str__(self):
        return '{}, {}'.format(self.usuario, self.tipo)

class Compromisso(models.Model):
    nome = models.CharField('nome', max_length=(50))
    dataHora = models.DateTimeField(null=False, blank=False)
    local = models.CharField('local', max_length=(50))
    nota = models.TextField()
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}, {}, {}'.format(self.agenda, self.nome, self.local, self.dataHora)

class Convite(models.Model):
    remetente = models.ForeignKey(User, on_delete=models.CASCADE)
    aceitar = models.BooleanField(default=False)
    convidados = models.ManyToManyField(User, related_name='convidados')
    compromisso = models.ForeignKey(Compromisso, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.remetente, self.aceitar)

