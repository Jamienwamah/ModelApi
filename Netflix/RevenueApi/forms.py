from django import forms
from .models import Input
# Create forms here

class MyForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = '__all__'
