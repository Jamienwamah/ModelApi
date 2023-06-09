# serializers allows complex datas such as querysets and model instance to be converted to native python datatypes 
#That can then be easily rendered by JSON, XML or other content types

from rest_framework import serializers
from .models import Predictions

class PredictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predictions
        fields = '__all__'