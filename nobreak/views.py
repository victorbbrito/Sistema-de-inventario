from django.shortcuts import render
from .models import Nobreak

def homenobreak(request):
    context ={}
    lista_nobreaks = Nobreak.objects.all().order_by('tombo')
    context['lista_nobreaks'] = lista_nobreaks
    return render(request, 'nobreaks.html', context)
