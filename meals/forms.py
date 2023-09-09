from django import forms 
from django.contrib.auth.models import User
from .models import Review

class Rating_form(forms.ModelForm):
    
    class Meta:
        model = Review
        fields= ['review']
    