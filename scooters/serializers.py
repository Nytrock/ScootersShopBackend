from .models import Scooter
from rest_framework.serializers import ModelSerializer


class ScooterSerializer(ModelSerializer):
    class Meta:
        model = Scooter
        fields = '__all__'