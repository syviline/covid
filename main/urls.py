from django.urls import path
from . import views
# Create your views here.

urlpatterns = [
    path('dev', views.development),
    path('', views.redirect_country),
    path('<str:country>', views.index),
]