from django import forms
from django.forms import ModelForm
from .models import MyCars

class MForm(ModelForm):
    class Meta:
        model = MyCars
        fields = '__all__'