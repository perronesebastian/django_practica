from django.shortcuts import render


# Create your views here.

def bienvenida(request):
    return render(request, 'inicio/index.html', {})

def bienvenido(request):
    return render(request, 'inicio/bienvenido.html', {})

def contacto(request):
    contexto = {
        'nombre': 'sebastian', 
        'lista_numeros': [1234123, 1234, 12354235, 6543544],
        'edad': 20
    }
    return render(request, 'inicio/contacto.html', contexto)