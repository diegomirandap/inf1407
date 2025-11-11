from carros.serializers import MTCarsSerializer
from rest_framework.views import APIView
from carros.models import MTCars
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CarsView(APIView):
    @swagger_auto_schema(
        operation_summary='Lista todos os carros',
        operation_description="Retorna uma lista de todos os carros disponíveis no banco de dados em ordem alfabética.",
        request_body=None, # opcional
        responses={200: MTCarsSerializer()}
    )
    def get(self, request):
        queryset = MTCars.objects.all().order_by('name')# importante informar que o queryset terá mais
        # de 1 resultado usando many=True
        serializer = MTCarsSerializer(queryset, many=True)
        return Response(serializer.data)