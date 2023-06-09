import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
# Create your views here.


class Prediction(APIView):
    def post(self, request):
        #data = request.data
        age = request.POST.get('age')
        gender = request.GET.get('gender')
        bp = request.Get.get('bp')
        cholesterol = request.GET.get('cholesterol')
        dtree = ApiConfig.model
        #predict using independent variables
        PredictionMade = data.predict([['age', 'gender', 'cholesterol', 'bp']])
        response_dict = {"Predicted drug": PredictionMade}
        print(response_dict)
        return Response(response_dict, status=200)