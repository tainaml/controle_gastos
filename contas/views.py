from django.shortcuts import render
from .models import Transacao


# Create your views here.

def home(request):
    data = {}
    data['transacoes'] = ['t1','t2','t3']

    return render(request,'contas/home.html',data)

def listagem(request):
    data = {}
    data['transaction'] = Transacao.objects.all()
    return render(request,'contas/listagem.html', data)



