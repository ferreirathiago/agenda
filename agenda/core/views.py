from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

#def index(request):
#    return redirect('/agenda/')

def lista_eventos(request):
    #evento = Evento.objects.get(id=1)
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)