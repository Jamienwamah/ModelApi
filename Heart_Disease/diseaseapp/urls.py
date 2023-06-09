from django.urls import path
from .views import *
#Create urls here

urlpatterns = [
    path('', Prediction.as_view(), name = 'Prediction'),
]