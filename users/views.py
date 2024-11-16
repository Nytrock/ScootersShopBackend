from django.contrib.auth import login, logout
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import LoginSerializer, UserSerializer




class SignupView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        summary='Регистрация пользователя',
        description='Регистрация нового пользователя по имени, паролю и почте',
        request=UserSerializer,
        responses={
            status.HTTP_200_OK: UserSerializer,
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                response=UserSerializer.errors,
                description='Выводит ошибки сериалайзера'),
        }
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        summary='Вход пользователя',
        description='Вход пользователя по имени и паролю. Информация о входе сохраняется на стороне пользователя',
        request=LoginSerializer,
        responses=None,
    )
    def post(self, request):
        serializer = LoginSerializer(data=self.request.data, context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_200_OK)


class LogoutView(APIView):

    @extend_schema(
        summary='Выход пользователя',
        description='Выход пользователя. На вход ничего не требует, выход происходит через метадату или вроде того',
        request=None,
        responses=None,
    )
    def post(self, request):
        logout(request)
        return Response(None, status=status.HTTP_200_OK)
