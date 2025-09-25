from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


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
    usuario1
    s@123456789
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

@login_required
def pagSecreta(request):
    '''
    Exibe a página secreta, acessível apenas para usuários autenticados
    O @login_required garante que apenas usuários logados possam acessar esta página
    '''
    return render(request, 'privado/pagSecreta.html')

def logout(request):
    '''
    Apresenta a página de confirmação de  logout
    '''
    return render(request, 'seguranca/logout.html')