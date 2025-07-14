from rest_framework import serializers
from .models import SensorData  # Importe o modelo SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData  # Use o modelo importado
        fields = '__all__'  # Inclui todos os campos do modelo