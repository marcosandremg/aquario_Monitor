from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView
from .models import SensorData
from .serializers import SensorDataSerializer

class SensorDataListCreate(generics.ListCreateAPIView):
    queryset = SensorData.objects.all().order_by('-timestamp')[:10]
    serializer_class = SensorDataSerializer

class LatestSensorData(APIView):
    def get(self, request):
        latest_data = SensorData.objects.last()
        if latest_data:
            serializer = SensorDataSerializer(latest_data)
            return Response(serializer.data)
        return Response(
            {"detail": "No data available"},
            status=status.HTTP_404_NOT_FOUND
        )
    
class DashboardView(TemplateView):
    template_name = 'monitor/dashboard.html'