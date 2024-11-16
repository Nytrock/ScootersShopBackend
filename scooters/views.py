from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListCreateAPIView
from .serializers import ScooterSerializer
from users.serializers import PurchaseSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, viewsets
from rest_framework import mixins
from rest_framework.views import APIView
from users.models import Purchase, User
from .models import Scooter
from rest_framework.response import Response
from users.models import Purchase
from drf_spectacular.utils import extend_schema, OpenApiResponse

class ScooterList(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class=ScooterSerializer
    queryset = Scooter.objects.all()
    @extend_schema(
        summary="Получение информации обо всех самокатах",
        description="Возвращает список всех самокатов.",
        responses={
            200: OpenApiResponse(response=ScooterSerializer(many=True), description="Список всех самокатов")
        }
    )
    def get(self, request):
        return self.list(request)
    
class ScooterDetail(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Scooter.objects.all()
    serializer_class = ScooterSerializer
    @extend_schema(
        summary="Получение информации о самокате по его id",
        description="Возвращает запись об одном самокате.",
        responses={
            200: OpenApiResponse(response=ScooterSerializer(many=True), description="Список всех самокатов"),
            404: OpenApiResponse(description="Самокат не найден")
        }
    )
    def get(self, request):
        return self.retrieve(request)
    
class ScooterBuy(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]
    @extend_schema(
        summary="Покупка самоката",
        description="Возвращает результат попытки покупки.",
        responses={
            201: OpenApiResponse(response=PurchaseSerializer, description="Покупка совершена успешно"),
            400: OpenApiResponse(description="Ошибки валидации")
        }
    )
    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    


