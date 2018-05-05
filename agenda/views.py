from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import Agenda, Compromisso

# Create your views here.

def listaAgendas(request):
    agendas = Agenda.objects.all()
    return render(request, "listaAgendas.html", context={"agendas":agendas})

def agendasPublDeUmDetUsuario(request, user_id):
    agendasPublicas = Agenda.objects.filter(tipo='Publica', usuario__id=user_id)
    return render(request, "agendasPublDeUmDetUsuario.html", context={"agendasPublicas":agendasPublicas})

def compromissosAgendaInst(request):
    compromissos = Compromisso.objects.filter(agenda__tipo='Institucional')
    return render(request, "compromissosAgendaInst.html", context={"compromissos":compromissos})


