from django.shortcuts import render
from .models import Controle

def homepage(request):
    return render(request, "index.html")

def homeusers(request):
    context = {}
    lista_users = Controle.objects.all().order_by('nome')
    context['lista_users'] = lista_users
    return render(request, 'users.html', context)

def contatos_page(request):
    return render(request, "contato.html")

def login_page(request):
    return render(request, "login.html")