from django.shortcuts import render
from .models import Transacao, Categoria
import datetime


def home(request):
    cat_names = {}
    cat_names['categoria'] = Categoria.objects.all()
    return render(request, 'contas/home.html', cat_names)




def listagem(request):
    data = {}
    x = {}
    data['transacoes'] = Transacao.objects.all()
    x['categorias'] = Categoria.objects.all()

    return render(request,'contas/listagem.html', x)





