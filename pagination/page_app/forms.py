from django import forms
from .models import *

class info_form(forms.ModelForm):
    

    class Meta:
        model= Info
        fields = '__all__'
 