from django.urls import path
from . import views
# Create your views here.

urlpatterns = [
    path('dev', views.development),
    path('region', views.region),
    path('', views.redirect_country),
    path('<str:country>', views.index),
    path('get_historical/<str:country>/<str:timespan>', views.getHistoricalStatistics)
]