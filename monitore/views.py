from django.shortcuts import render
from .models import Monitor

def homemonitor(request):
    context = {}
    lista_monitores = Monitor.objects.all().order_by('tombo')
    context['lista_monitores'] = lista_monitores
    return render(request, 'monitores.html', context)

