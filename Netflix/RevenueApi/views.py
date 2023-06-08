from django.shortcuts import render
from .forms import MyForm
from rest_framework import viewSets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Predictions
from .serializers import PredictionsSerializer
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
# Create your views here.

class PredictionsView(viewSets.ModelViewSets):
    querysets = Predictions.object.all()
    serializer_class = PredictionsSerializers
    
def MyForm(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=false)
           # myform.save()
        else:
            form = MyForm()
            # context = {'form': form}
            # return render(request, "myform/form.html", context)
        
        #Adding a decorator    
        @api_view([POST, GET, PUT, DELETE])
        def predict_accuracy(request):
            try:
                mdl = joblib.load("Desktop/ModelApi/ModelApi/Netflix/RevenueApi")
                mydata = request.data
                unit = np.array(list(mydata.values()))
                unit = unit.reshape(1, -1)
                
        
