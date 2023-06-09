from django import forms
from .models import Predictions
# Create forms here

class MyForm(forms.ModelForm):
    class Meta:
        model = Predictions
        fields = '__all__'
