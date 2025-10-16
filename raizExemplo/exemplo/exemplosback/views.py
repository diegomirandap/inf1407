from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

class ExemploClasse(APIView):
    def get(self, request):
        return Response({'mensagem':'Olá mundo!','msg': 'Resposta do método GET'}, status.HTTP_200_OK)

    def post(self, request):
        return Response({'mensagem':'Olá mundo!','msg': 'Resposta do método POST'}, status.HTTP_200_OK)

    def put(self, request):
        return Response({'mensagem':'Olá mundo!','msg': 'Resposta do método PUT'}, status.HTTP_200_OK)

    def delete(self, request):
        return Response({'mensagem':'Olá mundo!','msg': 'Resposta do método DELETE'}, status.HTTP_200_OK)

@api_view(('GET',)) #
@renderer_classes((JSONRenderer,)) #ambos requerem a virgula no fim para declarar como tupla
def exemploGET(request):
    return Response({'mensagem':'Olá mundo!','msg': 'Resposta da função GET'}, status.HTTP_200_OK)
    
@api_view(('POST',)) 
@renderer_classes((JSONRenderer,))
def exemploPOST(request):
    return Response({'mensagem':'Olá mundo!','msg': 'Resposta da função POST'}, status.HTTP_200_OK)

@api_view(('PUT','DELETE')) 
@renderer_classes((JSONRenderer,))
def exemploPUTDELETE(request):
    return Response({'mensagem':'Olá mundo!','msg': 'Resposta da função PUT ou DELETE'}, status.HTTP_200_OK)


