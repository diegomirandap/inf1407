from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from contatos.models import Pessoa
from contatos.forms import ContatoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
# Create your views here.

class ContatoCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = { 
            'formulario': ContatoModel2Form, 
            'titulo_pagina': 'Cria Contato',
            'titulo_janela': 'Criação de Contato',
            'botao': 'Cadastrar',
            }
        return render(request, "contatos/formContato.html", contexto)

    def post(self, request, *args, **kwargs):
        formulario = ContatoModel2Form(request.POST)
        if formulario.is_valid():
            contato = formulario.save()
            contato.save()
            return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))
        #Handler de erro nao esta funcionando
        else:
            contexto = { 
            'formulario': ContatoModel2Form, 
            'titulo_pagina': 'Cria Contato',
            'titulo_janela': 'Criação de Contato',
            'botao': 'Cadastrar',
            'mensagem': 'Cadastre corretamente'
            }
            return render(request, 'contatos/formContato.html', contexto)

class ContatoListView(View):
    def get(self,request,*args, **kwargs):
        pessoas = Pessoa.objects.all().order_by("nome")
        contexto = { 'pessoas': pessoas, }
        return render(
            request,
            'contatos/listaContatos.html',
            contexto)

class ContatoUpdateView(View):
    '''
    Exibe o formulário para atualizar um contato e processa a atualização
    '''
    def get(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        formulario = ContatoModel2Form(instance=pessoa)
        contexto = {
            'formulario': formulario, 
            'titulo_janela': 'Atualização de Contato',
            'titulo_pagina': 'Atualiza Contato',
            'botao': 'Atualizar',
            }
        return render(request, 'contatos/formContato.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        formulario = ContatoModel2Form(request.POST, instance=pessoa)
        if formulario.is_valid():
            pessoa = formulario.save() # cria uma pessoa com os dados do formulário
            pessoa.save() # salva uma pessoa no banco de dados
            return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))
        else:
            contexto = {
            'formulario': formulario, 
            'titulo_janela': 'Atualização de Contato',
            'titulo_pagina': 'Atualiza Contato',
            'botao': 'Atualiza',
            }
            return render(request, 'contatos/formContato.html', contexto)

class ContatoDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        contexto = { 'pessoa': pessoa, }
        return render(request, 'contatos/apagaContato.html', contexto)
    def post(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()
        return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))