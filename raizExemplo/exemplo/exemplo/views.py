from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

def home(request):
    '''
    Exibe a página inicial do site
    '''
    return render(request, 'exemplo/home.html')

def homeSec(request):
    '''
    Exibe a página inicial de segurança
    '''
    return render(request, 'seguranca/homeSec.html')

def registro(request):
    '''
    Exibe a página de registro de usuário
    s@12345678
    '''
    if request.method == 'POST':
        # Processa o formulário de registro aqui
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('homeSec')
        
    else:
        formulario = UserCreationForm()

    contexto = { 'form': formulario }
    return render(request, 'seguranca/registro.html', contexto)