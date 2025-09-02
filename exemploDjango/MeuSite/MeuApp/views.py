from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #processamento antes de mostrar a home page
    return render(request, 'MeuApp/home.html')

def SegundaPagina(request):
    #processamento antes de mostrar a segunda pagina
    return render(request, 'MeuApp/segundaPagina.html')