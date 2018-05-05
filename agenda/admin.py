from django.contrib import admin
from .models import Agenda, Compromisso, Convite

# Register your models here.

admin.site.register(Agenda)
admin.site.register(Compromisso)
admin.site.register(Convite)