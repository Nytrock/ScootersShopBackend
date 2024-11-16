from rest_framework import serializers
from rest_framework.serializers import Serializer


class SuccessSerializer(Serializer):
    status = serializers.CharField(default='Success')
