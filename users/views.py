from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import SuccessSerializer
from users.models import Customer, Purchase
from users.serializers import LoginSerializer, UserSerializer, BalanceSerializer, PurchaseSerializer, \
    PurchaseDeleteSerializer


class SignupView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        summary='Регистрация пользователя',
        description='Регистрация нового пользователя по имени, паролю и почте',
        request=UserSerializer,
        responses={
            status.HTTP_200_OK: SuccessSerializer(),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=UserSerializer.errors,
                description='Выводит ошибки сериалайзера'),
        }
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(SuccessSerializer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        summary='Вход пользователя',
        description='Вход пользователя по имени и паролю. Информация о входе сохраняется на стороне пользователя',
        request=LoginSerializer,
        responses=SuccessSerializer,
    )
    def post(self, request):
        serializer = LoginSerializer(data=self.request.data, context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(SuccessSerializer, status=status.HTTP_200_OK)


class LogoutView(APIView):

    @extend_schema(
        summary='Выход пользователя',
        description='Выход пользователя. На вход ничего не требует, выход происходит через метадату или вроде того',
        request=BalanceSerializer,
        responses={
            status.HTTP_200_OK: SuccessSerializer,
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=UserSerializer.errors,
                description='Выводит ошибки сериалайзера'),
        },
    )
    def post(self, request):
        logout(request)
        return Response(SuccessSerializer, status=status.HTTP_200_OK)


class AddBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Пополнение баланса',
        description='Пополнение баланса пользователя на передаваемую сумму (amount)',
        request=BalanceSerializer,
        responses=SuccessSerializer,
    )
    def post(self, request):
        serializer = BalanceSerializer(data=self.request.data, context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)

        customer = get_object_or_404(Customer.objects, id=request.user.id)
        customer.balance += serializer.validated_data['amount']
        customer.save()

        return Response(SuccessSerializer, status=status.HTTP_200_OK)


class PurchaseListView(ListAPIView):
    serializer_class = PurchaseSerializer
    model = serializer_class.Meta.model
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Purchase.objects.filter(user=self.request.user.id)
        return queryset


    @extend_schema(
        summary='Получить список заказов',
        description='Получение информации обо всех заказах пользователя',
        responses={
            200: OpenApiResponse(response=PurchaseSerializer(many=True), description='Список всех заказов пользователя')
        }
    )

    def get(self, request):
        return self.list(request)


class PurchaseDeleteView(DestroyAPIView):
    serializer_class = PurchaseDeleteSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Удаление покупки пользователя',
        description='Удаление покупки пользователя через её id',
        request=PurchaseDeleteSerializer,
        responses=SuccessSerializer,
    )
    def delete(self, request):

        return Response(SuccessSerializer, status=status.HTTP_200_OK)
