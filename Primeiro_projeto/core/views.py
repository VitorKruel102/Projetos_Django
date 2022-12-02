from django.shortcuts import render


def index(request):
    """."""
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado.'
    else:
        teste = 'Usuário dlogado.'
    ...
    context = {
        'curso': 'Programação web com Django Framework',
        'outro': 'Django é massa!',
        'logado': teste
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

