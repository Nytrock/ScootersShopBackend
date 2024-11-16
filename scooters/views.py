from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .serializers import ScooterSerializer
from rest_framework.permissions import AllowAny
from .models import Scooter
from drf_spectacular.utils import extend_schema, OpenApiResponse

class ScooterCreate(CreateAPIView):
    serializer_class=ScooterSerializer
    permission_classes = (AllowAny,)
    @extend_schema(
        summary="Добавление самоката в базу данных",
        description="Создаёт новый самокат с уникальным названием, описанием и стоимостью за минуту. "
                    "Макс длина названия - 100 символов."
                    "Макс длина описания - 100 символов."
                    "Макс цена - 100 р./мин",
        request=ScooterSerializer,
        responses={
            201: OpenApiResponse(response=ScooterSerializer, description="Самокат успешно создан"),
            400: OpenApiResponse(description="Ошибки валидации")
        }
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ScooterList(ListAPIView):
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
    
class ScooterDetail(RetrieveAPIView):
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