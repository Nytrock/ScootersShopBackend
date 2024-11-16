from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from users.models import Customer, Purchase


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        Customer.objects.create(
            id=user.id,
            user=user,
        )
        return user


class LoginSerializer(Serializer):
    username = serializers.CharField(
        label='Username'
    )
    password = serializers.CharField(
        label='Password',
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                raise serializers.ValidationError('Access denied: wrong username or password.', code='authorization')
        else:
            raise serializers.ValidationError('Both "username" and "password" are required.', code='authorization')
        attrs['user'] = user
        return attrs


class BalanceSerializer(Serializer):
    amount = serializers.IntegerField(
        label='Amount',
        write_only=True
    )

class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class PurchaseDeleteSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id']
