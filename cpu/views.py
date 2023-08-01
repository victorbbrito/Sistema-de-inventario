from django.shortcuts import render
from .models import Cpu

def homecpus(request):
    context = {}
    lista_cpus = Cpu.objects.all().order_by('tombo')
    context['lista_cpus'] = lista_cpus
    return render(request, 'cpus.html', context)
# Create your views here.
