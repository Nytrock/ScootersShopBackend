from rest_framework import serializers
from rest_framework.serializers import Serializer


class StatusSerializer(Serializer):
    status = serializers.IntegerField()