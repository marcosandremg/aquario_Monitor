#from django.urls import path
#from .views import SensorDataListCreate, LatestSensorData, DashboardView

#urlpatterns = [
#    path('api/data/', SensorDataListCreate.as_view(), name='sensor-data-list'),
#    path('api/latest/', LatestSensorData.as_view(), name='latest-sensor-data'),
#    path('dashboard/', DashboardView.as_view(), name='dashboard'),
#]
from django.urls import path
from .views import DashboardView, SensorDataListCreate, LatestSensorData

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('api/data/', SensorDataListCreate.as_view(), name='sensor-data-list'),
    path('api/latest/', LatestSensorData.as_view(), name='latest-sensor-data'),
]
