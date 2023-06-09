from django.urls import path, include
from . import views
from rest_framework import routers

#Create urls here

router = routers.DefaultRouter()
router.register('MyApi', views.PredictionsView, basename='MyApi')
urlpatterns = [
    path('form/', views.MyForm),
    path('api/', include(router.urls)),
    path('status/', views.approve_reject),
]