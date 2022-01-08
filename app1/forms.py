from django import forms
from .models import *


class MyForm(forms.ModelForm):
    
    class Meta:
        model = myform
        fields = '__all__'


