from django.shortcuts import render
from .forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Predictions
from .serializers import PredictionsSerializer
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
# Create your views here.

class PredictionsView(viewsets.ModelViewSet):
    querysets = Predictions.objects.all()
    serializer_class = PredictionsSerializer
    basename = 'Predictions'
    
def MyForm(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=false)
           # my_form.save()
        else:
            form = MyForm()
            # context = {'form': form}
            # return render(request, "my_form/form.html", context)
        
        #Adding a decorator    
        @api_view([POST, GET, PUT, DELETE])
        def approve_reject(request):
            try:
                mdl = joblib.load("Home/Desktop?ModelApi/ModelApi/Netflix/RevenueApi/Predicting_heart_disease_model.pkl")
                my_data = request.data
                unit = np.array(list(my_data.values()))
                unit = unit.reshape(1, -1)
                y_pred = mdl.predict(X)
                y_pred = y_pred(0.58)
                new_df = pd.DataFrame(y_pred, Columns= ['Status'])
                new_df = new_df.replace({True: 'approved', False: 'Rejected' })
                return JsonResponse('Your status is {}'.format(new_df), safe = False)
            except ValueError as e:
                return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
                
        
